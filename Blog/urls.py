from django.urls import path
from . import views



urlpatterns = [
    path('', views.Blogview.as_view(template_name = 'blog/Post_list.html'), name = "PostList" ),
    path('<int:pk>/', views.Postview.as_view(template_name = 'blog/post.html'), name = "Postview" ),
    path('create', views.CreatePostView.as_view(template_name = 'blog/CreatePost.html'), name = "CreatePostView"),
    path('comment', views.CreateCommentview.as_view(template_name = 'blog/Createcomment.html'), name = "CreateCommentView")


]