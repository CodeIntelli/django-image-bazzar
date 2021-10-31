from django.shortcuts import render
from .models import ImageDB, Category
# Create your views here.


def home(request):
    images = ImageDB.objects.all()
    cats = Category.objects.all()
    return render(request, 'index.html', {"images": images, "cats": cats})


def categories(request, id):
    print(id)
    cats = Category.objects.all()
    category = Category.objects.get(id=id)
    images = ImageDB.objects.filter(cat=category)
    return render(request, 'index.html', {"images": images, "cats": cats})
