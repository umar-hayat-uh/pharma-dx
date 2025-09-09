"""
URL configuration for PharmaDX project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import render
from django.urls import path


def home(request):
    return render(request, 'home.html')

def drug_interaction(request):
    return render(request, 'drug-interaction.html')

def drug_finder(request):
    return render(request, 'drug-finder.html')

def dosage_calculator(request):
    return render(request, 'dosage-calculator.html')

def amr_checker(request):
    return render(request, 'amr-checker.html')

def pharmacopedia(request):
    return render(request, 'pharmacopedia.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('drug-interaction/', drug_interaction, name='drug-interaction'),
    path('drug-finder/', drug_finder, name='drug-finder'),
    path('dosage-calculator/', dosage_calculator, name='dosage-calculator'),
    path('amr-checker/', amr_checker, name='amr-checker'),
    path('pharmacopedia/', pharmacopedia, name='pharmacopedia'),
]

