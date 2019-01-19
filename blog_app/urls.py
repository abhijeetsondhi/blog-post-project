from django.conf.urls import url,include
from blog_app import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'blog_app'

urlpatterns = [
            url(r'^$',views.PostList.as_view(),name='post_list'),
            url(r'^post/(?P<pk>\d+)/add/$',views.add_friend,name='add_frnd'),
            url(r'^user/(?P<pk>\d+)/profile/$',views.user_profile,name='user_prof'),
            url(r'^listuser/$',views.ListUser.as_view(),name='list_user'),
            url(r'^post/(?P<pk>\d+)/friendlist/$',views.friend_list,name='frnd_list'),
            url(r'^about/$',views.AboutView.as_view(),name='about'),
            url(r'^post/(?P<pk>\d+)/$',views.BlogPost.as_view(),name='blog_post'),
            url(r'^post/login/$',views.CreatePost.as_view(),name='post_login'),
            url(r'^post/(?P<pk>\d+)/edit/$',views.BlogUpdate.as_view(),name='post_edit'),
            url(r'^post/(?P<pk>\d+)/delete$',views.PostDelete.as_view(),name='post_delete'),
            url(r'^drafts/$',views.DraftList.as_view(),name='drafts_list'),
            url(r'^post/(?P<pk>\d+)/comment/$',views.add_comment_to_post,name='post_comment'),
            url(r'^post/(?P<pk>\d+)/approve/$',views.comment_approval,name='comment_approval'),
            url(r'^post/(?P<pk>\d+)/delete/$',views.comment_delete,name='comment_delete'),
            url(r'^post/(?P<pk>\d+)/publish/$',views.publish_post,name='publish_post'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
