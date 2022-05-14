from django.shortcuts import render
from django.http import HttpResponse
import datetime


def test(request):
    return HttpResponse('<h1>Привет укажите (info) в адресной строке чтобы перейти на другую строницу.</h1>')


def test1(request):
    dict_ = {
        'title': 'afisha APPLICATION',
        'text': 'укажите (time) в адресной строке чтобы перейти на другую строницу.'
    }
    return render(request, 'info.html', context=dict_)


def test2(request):
    now = datetime.datetime.now()
    return HttpResponse(f'<h1>{now}</h1>')

# Create your views here.
