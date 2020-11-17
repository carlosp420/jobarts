from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('jobs/', views.jobs, name="jobs"),
    path('detail/<str:pk>/', views.detail, name="detail"),

]
