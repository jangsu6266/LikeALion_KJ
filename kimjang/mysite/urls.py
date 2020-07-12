"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import  path

from bookmark.views import BookmarkLV,BookmarkDV
import blog.views


app_name = 'bookmark'
urlpatterns = [
    path('admin/', admin.site.urls),
    #class-based views
    #path('bookmark/', BookmarkLV.as_view(), name='index'),
    #path('bookmark/<int:pk',BookmarkDV.as_view(), name='detail'),
    path('', blog.views.home, name = "home"),
    path('blog/<int:blog_id>', blog.views.detail, name= "detail"),

    #path('bookmark/', include('bookmark.urls')),
    path('blog/new/', blog.views.new, name="new"),
    path('blog/create/', blog.views.create, name="create"),
    path('blog/delete/<int:blog_id>', blog.views.delete, name="delete"),
    path('blog/edit/<int:blog_id>', blog.views.edit, name="edit"),
    path('blog/update/<int:blog_id>', blog.views.update, name="update"),
    path('blog/comment/<int:blog_id>', blog.views.add_comment_to_post, name="add_comment_to_post"),
]
