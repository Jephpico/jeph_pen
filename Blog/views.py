from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Comment
from django.urls import reverse_lazy



# Create your views here.
class Blogview(ListView):
     model = Post
     template_name = 'blog/Post_list.hmtl'
    



class Postview(DetailView):
   model = Post
   template_name = 'blog/Post.html'

class CreatePostView(CreateView):
    model = Post
    fields = ['title','slug','body', 'author']
    template_name = 'blog/CreatePost.html'
    success_url = reverse_lazy('PostList')


class CommentView(DetailView):
    model = Comment
    #fields = ['name', 'body']
    template_name = 'blog/Post.html'


class CreateCommentview(CreateView):
    model = Comment
    fields = ['name','body',]
    template_name = 'blog/Createcomment.html'
    success_url = reverse_lazy('home')

   
