from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(FacebookComment)
admin.site.register(FacebookUser)
admin.site.register(FacebookPage)
admin.site.register(FacebookPost)
admin.site.register(Feed)
admin.site.register(Word)
admin.site.register(Tracked_Word)
admin.site.register(Article)