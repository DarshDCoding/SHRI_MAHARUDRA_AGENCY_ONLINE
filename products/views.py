from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def products_page(request):
    return HttpResponse("<h1>This is the product page.</h1>")

