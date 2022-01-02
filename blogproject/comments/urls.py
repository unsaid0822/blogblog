# -*- coding:utf-8 -*-
# @Time    : 2022/1/2 16:25
# @Author  : Muzzily
# @desc    :
from django.contrib import admin
from django.urls import path, include

from comments import views

app_name = "comments"

urlpatterns = [
    path('comment/<int:post_pk>', views.comment, name='comment'),
]
