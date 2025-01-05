from django.http import HttpResponse, HttpResponseNotFound, Http404

from django.shortcuts import render


def index(request):
    return HttpResponse('Hello World!')


def categories(request, cat_id):
    return HttpResponse(f'<h1>Categories</h1><p>id: {cat_id}</p>')


def categories_by_slug(request, cat_slug):
    if request.GET:
        if request.GET:
            return HttpResponse(f'{"|".join(f"{k}={v}" for k, v in request.GET.items())}')
    return HttpResponse(f'<h1>Categories by slug</h1><p>slug : {cat_slug}</p>')


def archive(request, year):
    if year > 2025:
        raise Http404
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')

