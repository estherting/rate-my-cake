from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^amadon$', views.amadon),
    url(r'^amadon/process$', views.process),
    url(r'^amadon/checkout$', views.checkout),
]
