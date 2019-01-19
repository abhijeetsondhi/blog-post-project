from django.contrib import admin
from blog_app.models import Post,Comment,Friend,UserProfileInfo
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Friend)
admin.site.register(UserProfileInfo)
