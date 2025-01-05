from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponseServerError

from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string
from datetime import datetime


menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'float': 25.5,
        'set': {1, 2, 3, 4, 5},
        'dict': {'key1': 'value1', 'key2': 'value2'},
        'obj': MyClass(10, 20)
    }
    return render(request, 'women/index.html', context=data)


def about(request):
    data = {
        'title': 'О сайте',
    }
    return render(request, 'women/about.html', data)

def categories(request, cat_id):
    return HttpResponse(f'<h1>Categories</h1><p>id: {cat_id}</p>')


def categories_by_slug(request, cat_slug):
    if request.GET:
        if request.GET:
            return HttpResponse(f'{"|".join(f"{k}={v}" for k, v in request.GET.items())}')
    return HttpResponse(f'<h1>Categories by slug</h1><p>slug : {cat_slug}</p>')


def archive(request, year):
    if year > datetime.now().year:
        uri = reverse('cats', args=('music', ))
        return HttpResponseRedirect(uri)
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')


def server_error(request):
    return HttpResponseServerError('<h1>Сервер сказал пошел ты 500раз</h1>')

