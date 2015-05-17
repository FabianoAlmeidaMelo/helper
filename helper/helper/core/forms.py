# coding: utf-8

from django import forms

from .models import (
    Developer,
)


class DeveloperForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = ('name', )
