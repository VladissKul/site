from django.shortcuts import render
from .models import Project


def home(request):
    projects = Project.objects.all()  # импортируем все данные из БД
    return render(request, 'portfolio/home.html', {'projects': projects})
