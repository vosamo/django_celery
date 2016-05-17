#!/usr/bin/env python
# coding=utf-8

from django.conf.urls import url
from main import views
urlpatterns = [
    url(r'^$', views.NewTask.as_view()),
    url(r'^(?P<uuid>[\w\d-]+)/$', views.TaskState.as_view()),
]
