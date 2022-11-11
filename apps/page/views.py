from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from .models import Page
from django.urls import reverse_lazy
# Create your views here.

class PageCreateView(CreateView):
    model = Page
    fields = "__all__"
    template_name = "create.html"
    success_url = reverse_lazy("home_paginas")

class PagesListView(ListView):
    model = Page
    template_name = "list.html"

class PageHTML(DetailView):
    model = Page
    template_name = "page.html"