# -*- coding:utf-8 -*-
# @Time    : 2022/1/2 16:19
# @Author  : Muzzily
# @desc    :
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']