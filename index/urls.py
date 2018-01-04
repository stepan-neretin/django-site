from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from . import views
from .models import Articles
urlpatterns = [
   url(r'^$', views.index, name='index'),
   url(r'^$', ListView.as_view(queryset=Articles.objects.all().order_by("-date")[:20]))
]