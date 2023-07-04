from django.http import HttpRequest,  HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    """
    This is the entry point of the website
    @param request: HttpRequest
    @return: render of the index.html template
    """
    context = {}
    return render(request, 'core/index.html', context)
