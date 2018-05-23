from django.conf.urls import url, static
from . import views
from django.conf import settings


urlpatterns = [
    url(r'^$', views.index),
    url(r'^blogs/new$', views.new),
    url(r'create$', views.create),
    url(r'(?P<blogNum>\d+)$', views.show),
    url(r'(?P<blogNum>\d+)/edit$', views.edit),
    url(r'(?P<blogNum>\d+)/delete$', views.destroy),
    url(r'^upload_file$', views.upload_file),
    url(r'^success/upload$', views.success_upload)
]
