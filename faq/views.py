from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from .models import Category, Faq
# Create your views here.

def category(request):
    categories = Category.objects.all()
    return render(request, 'faq/category.html', {'categories':categories,})

def faq(request, category_id):
    faq = Faq.objects.filter(category_id = category_id)
    return render(request, 'faq/questions.html', {'faq':faq,})