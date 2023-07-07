import this
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from accounts.models import Customers
 
def changepass(request):
    return render(request,'changepass.html')
   