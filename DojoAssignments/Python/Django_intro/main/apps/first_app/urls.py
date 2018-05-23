from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),   # at the root of url, have it be handled by views, index method
    url(r'^test$', views.test)
]
