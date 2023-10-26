from django.urls import path
from . import views


app_name= 'app_blog'


urlpatterns = [
    path ('', views.BlogList.as_view(), name='blog_list'),
    path('Write/', views.createBlog.as_view(), name= 'create_blog'),
    path('blog_details/<int:pk>', views.blog_details, name='blog_details'),
    path('liked/<int:pk>', views.liked , name= 'liked_post'),
    path('unliked/<int:pk>', views.unliked ,name ='unliked_post'),
    path('my-blog/' , views.MyBlogs.as_view() , name='my_blogs'),
    path('Edit-blog/<int:pk>' , views.UpdateBlog.as_view() , name ='edit_blog'),
    
]