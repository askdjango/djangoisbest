from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<post_pk>\d+)/comments/new/$', views.comment_new, name='comment_new'),
]

