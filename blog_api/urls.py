from .views import AdminPostDetail, CreatePost, DeletePost, EditPost, PostDetail, PostList, PostListDetailfilter
from rest_framework.urls import path

app_name = "blog_api"

urlpatterns = [
    path('', PostList.as_view(),name="postlist"),
    path('<str:slug>/', PostDetail.as_view(),name="postdetail"),
    path('search/', PostListDetailfilter.as_view(),name="customsearch"),
    
    # Admin Urls
    path('admin/create/',CreatePost.as_view(),name="createpost"),
    path('admin/edit/postdetail/<int:pk>/',AdminPostDetail.as_view(),name="adminpostdetail"),
    path('admin/edit/<int:pk>/',EditPost.as_view(),name="editpost"),
    path('admin/delete/<int:pk>/',DeletePost.as_view(),name="deletepost"),
]
    

