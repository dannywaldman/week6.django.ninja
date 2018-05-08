from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process_money/(?P<action>[A-z]+$)', views.process_money)
]
