from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_main_template, name="home"),
    path('about', views.about, name="about"),
]