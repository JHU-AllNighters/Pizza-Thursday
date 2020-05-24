from django.shortcuts import render

from .utils import main


def index(request):
    return render(request, "home.html")


def external(request):
    shared_url = request.POST.get("shared_url")
    costs = main(shared_url)
    return render(request, "home.html", {"costs": costs})
