from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponseServerError

from django.shortcuts import render, redirect, get_object_or_404
from .models import Women
from django.urls import reverse
from django.template.loader import render_to_string
from datetime import datetime
from django.template.defaultfilters import slugify

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли',
     'content': '''<h1>Анджелина Джоли</h1> (англ. Angelina Jolie[7], при рождении Войт (англ. Voight), ранее Джоли Питт (англ. Jolie Pitt); род. 4 июня 1975, Лос-Анджелес, Калифорния, США) — американская актриса кино, телевидения и озвучивания, кинорежиссёр, сценаристка, продюсер, фотомодель, посол доброй воли ООН. 
     Обладательница премии «Оскар», трёх премий «Золотой глобус» (первая актриса в истории, три года подряд выигравшая премию) и двух «Премий Гильдии киноактёров США».''',
     'is_published': True},
    {'id': 2, 'title': 'Margo', 'content': 'Bio of Margo', 'is_published': 1},
    {'id': 3, 'title': 'Julia', 'content': 'Bio of Julia', 'is_published': False},
]

cats_db = [
    {'id': 1, 'name': 'Актрисы'},
    {'id': 2, 'name': 'Певицы'},
    {'id': 3, 'name': 'Спортсменки'},
]


def index(request):
    data = {
        'title': 'Главная страница',
        'posts': Women.objects.filter(is_published=1),
        'selected_category': 0,
    }
    return render(request, 'women/index.html', context=data)


def about(request):
    data = {
        'title': 'О сайте',
    }
    return render(request, 'women/about.html', data)


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    data = {
        'title': post.title,
        'post': post,
        'cat_selected': 1
    }
    return render(request, 'women/post.html', data)


def add_page(request):
    return HttpResponse('Добавление статьи')


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def show_category(request, cat_id):
    data = {
        'title': 'Отображение по рубрикам',
        'posts': list(filter(lambda x: x['is_published'], data_db)),
        'selected_category': cat_id,
    }
    return render(request, 'women/index.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')


def server_error(request):
    return HttpResponseServerError('<h1>Сервер сказал пошел ты 500раз</h1>')
