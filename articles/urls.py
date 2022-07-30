from django.urls import path ,include
#from django.conf.urls import  include, path

from . import views

app_name = 'articles'
urlpatterns = [
    path('',views.article_list,name="list"),
    path('articles/<slug:slug>/',views.article_detail,name="detail")
]
