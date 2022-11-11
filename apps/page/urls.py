from django.urls import path
from .views import PageCreateView, PagesListView, PageHTML

urlpatterns = [
    path("", PagesListView.as_view(), name="home_paginas"),
    path("/create/", PageCreateView.as_view(), name="criar_pagina"),
    path("<pk>", PageHTML.as_view(), name="page")
]