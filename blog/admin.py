from django.contrib import admin
from .models import Post, Publication, UserProfile, PageWithTests

admin.site.register(Post)
admin.site.register(Publication)
admin.site.register(UserProfile)
admin.site.register(PageWithTests)

