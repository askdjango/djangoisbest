from django.shortcuts import get_object_or_404, render, resolve_url
from django.views.generic import ListView, DetailView, CreateView
from blog.models import Post, Comment
from blog.forms import CommentForm


post_list = ListView.as_view(model=Post)

post_detail = DetailView.as_view(model=Post)


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = get_object_or_404(Post, pk=self.kwargs['post_pk'])
        return super(CommentCreateView, self).form_valid(form)

    def get_success_url(self):
        return resolve_url('blog:post_detail', self.kwargs['post_pk'])

comment_new = CommentCreateView.as_view()

