"""
プロジェクトコアのビュー
"""
from django.shortcuts import render
from django.http import HttpRequest


def index(request: HttpRequest):
    """
    初期表示
    @param request
    @param form
    @return: django template
    """
    return render(request, 'index.dhtml')
