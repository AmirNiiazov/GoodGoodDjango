from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return HttpResponse("Hello, world. You're at the")


def categories(request, cat_id):
    return HttpResponse(f"<h1>Category</h1><h2>int {cat_id}</h2>")


def categories_by_slug(request, cat_slug):
    # print(request.GET)
    # print(request.POST)
    return HttpResponse(f"<h1>Category</h1><h2>slug {cat_slug}</h2>")


def archive(request, year):
    if year > 2024:
        url = reverse('cats', args=('music',))
        # return redirect(url, permanent=True)
        return HttpResponsePermanentRedirect(url)

    return HttpResponse(f"<h1>Category</h1><h2>year {year}</h2>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


