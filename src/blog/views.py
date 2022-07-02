from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, "blog\\index.html")


def art(request, article_number):
    if article_number in ["01", "02", "03"]:
        return render(request, f"blog\\article_{article_number}.html")
    return render(request, "blog\\article_not_found.html")
