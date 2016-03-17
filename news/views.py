from django.shortcuts import render, redirect
import http.cookiejar, urllib.request
from .models import Article, Feed
from .forms import FeedForm
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import feedparser
import datetime
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def articles_list(request):
    articles = Article.objects.all().order_by('-publication_date')
    rows = [articles[x:x+1] for x in range(0, len(articles), 1)]
    # return render(request, 'news/articles_list.html', {'rows': rows})

    paginator = Paginator(articles, 25) # Show 25 articles per page

    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)

    # context = {
    # 'object_list':rows,
    # 'title' : 'list'
    # }

    return render(request, 'news/articles_list.html', {'rows' : rows})


@csrf_exempt
def ajax_articles(request):
    rows = []
    if request.method =="GET":
        try:
            date_from = datetime.datetime.strptime(request.GET['date_from'], "%Y-%m-%d")
        except:
            date_from = datetime.date.today() - datetime.timedelta(days=5)
        try:
            date_to = datetime.datetime.strptime(request.GET['date_to'], "%Y-%m-%d").replace(hour=23, minute=59, second=59)
        except:
            date_to = datetime.date.today().replace(hour=23, minute=59, second=59)
        articles = Article.objects.filter(publication_date__range=[date_from, date_to]).order_by('-publication_date')
        rows = [articles[x:x+1] for x in range(0, len(articles), 1)]

    return render(request, 'news/articles_cycle.html', locals())# {'rows' : rows})


###Feeds Listing
def feeds_list(request):
    feeds = Feed.objects.all()
    return render(request, 'news/feeds_list.html', {'feeds': feeds})


def new_feed(request):
    if request.method == "POST":
        form = FeedForm(request.POST)
        if form.is_valid():
            feed = form.save(commit=False)

            existingFeed = Feed.objects.filter(url = feed.url)
            if len(existingFeed) == 0:
                feedData = feedparser.parse(feed.url)

                # set some fields
                feed.title = feedData.feed.title
                feed.save()

                for entry in feedData.entries:
                    article = Article()
                    article.title = entry.title
                    article.url = entry.link
                    article.description = entry.description
                    cj = http.cookiejar.CookieJar()
                    # opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
                    # url_open = opener.open(article.url)
                    # article.content = url_open.read()                    
                    # article.content = urlopen(article.url).read()

                    d = datetime.datetime(*(entry.published_parsed[0:6]))
                    dateString = d.strftime('%Y-%m-%d %H:%M:%S')

                    article.publication_date = dateString
                    article.feed = feed
                    article.save()

            return redirect('news.views.feeds_list')
    else:
        form = FeedForm()
    return render(request, 'news/new_feed.html', {'form': form})