# -*- coding:utf-8 -*-
from django import forms


class TextForm(forms.Form):
    a = forms.CharField()
