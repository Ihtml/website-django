# _*_ coding: utf-8 _*_
__author__ = 'ife'
__date__ = '2018-12-04 22:12'

from django.urls import path
from django.views.generic import TemplateView
from . import views


# 命名空间
app_name = 'courses'
urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name="index"),
]