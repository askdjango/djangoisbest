from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Post


post_list = ListView.as_view(model=Post)

