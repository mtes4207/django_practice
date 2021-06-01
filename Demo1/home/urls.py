from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('simple_crawl/', views.simple_crawl),
    path('result_crawl/',views.POST_crawl),

]