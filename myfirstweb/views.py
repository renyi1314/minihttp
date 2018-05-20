from django.http import HttpResponse
from django.shortcuts import render


def myweb(request):
    return render(request, 'js_add_sub.html')


def test(request):
    return render(request, 'test.html')
