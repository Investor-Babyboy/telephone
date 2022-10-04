from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from .form import TelephoneForm
from .models import Telephone

# Create your views here.

def homepage(request):
    context = {
        "details" : Telephone.objects.all()
    }
    return render(request, 'telephone/homepage.html', context)

def add(request):
    form = TelephoneForm(request.POST or None,)
    context = {
        'form': form
    }
    if  form.is_valid():
        form.save()
        return redirect(reverse('homepage'))
    return render(request, 'telephone/add.html', context)

def cancel(request, id):
    history=Telephone.objects.get(id=id)
    history.delete()
    messages.success(request, 'record deleted')
    return redirect (reverse('homepage'))

def alter(request, id):
    history=Telephone.objects.get(id=id)
    form = TelephoneForm(request.POST or None, request.FILES or None, instance=history)
    context= {
        'form': form
    }
    if form.is_valid():
        form.save()
        return redirect(reverse('homepage'))
    return render(request, 'telephone/alter.html', context)

