from django.shortcuts import render, HttpResponse, redirect
# Create your views here.

def home(request):
    return render(request, 'taifa/index.html')



def account(request):
    context = {}
    return render(request, 'taifa/account.html', context)