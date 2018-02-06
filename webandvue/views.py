# coding: utf-8
from django.shortcuts import render
from django.conf.urls import url
from django.shortcuts import render_to_response
from django.views.generic.base import View


class TopView(View):
    """自定义"""
    def get(self, request, *args):
        # a = reverse('add2', args=args)
        # print(a)
        return render_to_response('dist/index.html')


urlpatterns = [
    url('', TopView.as_view(), name='v'),
]