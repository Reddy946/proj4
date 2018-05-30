from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
def input(request):
    return render(request,'input.html')
def insert(request):
    pid1=int(request.GET['t1'])
    pname1=request.GET['t2']
    pcost1=float(request.GET['t3'])
    pmfd1=request.GET['t4']
    pexpd1=request.GET['t5']
    f=Product(pid=pid1,pname=pname1,pcost=pcost1,pmfd=pmfd1,pexpdt=pexpd1)
    f.save()
    return HttpResponse("data inserted successfully")




