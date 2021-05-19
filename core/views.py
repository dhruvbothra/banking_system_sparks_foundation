from django.shortcuts import redirect, render
from .models import *
# Create your views here.

def home(request):
    return render(request,"home.html")

def customer(request):
    customer=Customer.objects.all()
    dict={
        'customer':customer
    }
    return render(request,"customers.html",dict)

def transfer(request,id):
    trans=Customer.objects.get(id=id)
    cus=id
    print(cus)
    customer=Customer.objects.exclude(name=trans.name)
    trans_dic={
        "trans":trans,
        "customer":customer
    }
    return render(request,"transfer.html",trans_dic)


def transfer_processing(request,id):
    if request.method=="POST":
        transferby=request.POST["transferby"]
        transferto=request.POST["transferto"]
        amount=request.POST["amount"]
        cus=Customer.objects.get(id=id)
        history=History(transferto=transferto,transferby=transferby,amount=amount)
        if cus.balance >= float(history.amount):
            cus.balance=cus.balance-float(history.amount)
            cus.save()
            history.save()
            return redirect("/customer")
        else:
            return redirect("/customer")    

def history(request):
    history=History.objects.all()
    his_dic={
        "history":history
    }
    return render(request,"history.html",his_dic)