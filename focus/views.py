# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Article
from .forms import LoginForm
from django.shortcuts import render

# Create your views here.
def index(request):
    latest_article_list = Article.objects.query_by_time()
    loginform = LoginForm()
    context = {'latest_article_list': latest_article_list, 'loginform': loginform}
    return render(request, 'index.html', context)