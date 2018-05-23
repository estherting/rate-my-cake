from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'generate_word$', views.makeWord),
    url(r'reset$', views.reset)
]
