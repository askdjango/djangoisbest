from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]

