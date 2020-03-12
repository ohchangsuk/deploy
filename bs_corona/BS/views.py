from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def phar(request):
        return render(request, "BS/phar.html")

@csrf_exempt
def index(request):
        return render(request, "BS/index.html")
@csrf_exempt
def More(request):
        return render(request, "BS/More.html")