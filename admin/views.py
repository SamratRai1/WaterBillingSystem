from ast import Return
from asyncio.windows_events import NULL
import email
from http.client import HTTPResponse
import re
from this import d
from turtle import pos, position
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from accounts.models import Customers,Rates, Revenue
from admin.models import Users
from django.contrib import messages 
from admin.forms import userforms,customerforms,ratesforms
from django.contrib import messages
from random import randrange
import json
#from accounts.models import Users as sa
# # Create your views here.
# Registers new employee into the database
def registerWorkers(request,position):
    if request.method == 'POST':
        cust = Users.objects.all()
            
        email = request.POST.get('email')
        email = email.lower()
        citizenship = request.POST.get('citizenship')
                  
        if cust.filter(email=email).exists() or cust.filter(citizenship=citizenship).exists():
            print('email taken')
            if (position == 'Counter'):
                return redirect('counter')
            return redirect('registermeter')
        else:
            saverecord = Users(email=email,citizenship=citizenship,password="Pass",position=position)
            saverecord.save()
            print('user created')
            if position=="Counter":
                return redirect('counter')
            else:
                return redirect('reader')    
    else:
        if (position=="Counter"):
            return render(request,'counter.html')
        else:    
            return render(request,'meterreader.html')

# Returns the list of  employee details from the table that contains the given position
def displayWorker(request,position):
    showall=Users.objects.get(position=position)
    if (position == 'Counter'):
        return render(request,'editcountertable.html',{"data":showall})
    return render(request,'editmeterreadertable.html',{"data":showall})

def displaymeterreader(request):
    showall=Users.objects.filter(position='Meterreader')
    return render(request,'editmeterreadertable.html',{"data":showall})

 # Get the matching column from the table and redirects the web page as needed   
def editWorker(request,email,position):
    
    editobj=Users.objects.get(email=email)
    if (position == 'Counter'):
        return render(request,'editcounter.html',{"Users":editobj})
    return render(request,'editmeterreader.html',{"Users":editobj})

# Gets data from the user and updates the new data in the table
def updateWorker(request,email,position):
    updateData=Users.objects.get(email=email)   
    form=userforms(request.POST,instance=updateData)
    if form.is_valid():
        form.save()
        messages.success(request,'Record successfull')
        if(position=="Counter"):
            return render(request,'editcounter.html',{"Users":updateData})
        return render(request,'editmeterreader.html',{"Users":updateData})
    if (position=="Counter"):
        return render(request,'editcounter.html',"Failed" )
    return render(request,'editmeterreader.html',"Failed" )            

#Function for deleting a user after taking the email that needs to be deleted
def deleteusers(request,email):
    try:
        delusers=Users.objects.get(email=email)
        
        position=delusers.position
        #return HttpResponse(position)
        delusers.delete()
        showall=Users.objects.all().filter(position=position)
        # return HttpResponse(showall.position)
        if position=="Customer":
            delcust=Customers.objects.get(email=email)  
            delcust.delete()
            showdata=Customers.objects.all()   
            return redirect('customer')
        elif position=="Counter": 
            return redirect('displaycountertable')    
        else:
            # return HttpResponse(showall)
            return redirect("displaymeterreader")
    except:
        delcust=Customers.objects.get(email=email)
        delcust.delete()
        return redirect('customer')

#updates the status of customer into true and adds the customer into the user table
def activateusers(request,email):
    cust=Customers.objects.get(email=email)
    thisdict={"customername":cust.customername,"email":cust.email,"citizenship":cust.citizenship,"address":cust.address,"password":cust.password,"status":True,"currentunit":cust.currentunit,"discountamount": cust.discountamount ,"fineamount":cust.fineamount,"previousunit":cust.currentunit,"totaldue":cust.totaldue,"meternum":cust.meternum}
    # return HTTPResponse(thisdict)          
    form=customerforms(thisdict,instance=cust)
    if form.is_valid():
        form.save()
        saverecord = Users(email=cust.email,citizenship=cust.citizenship,password=cust.password,position="Customer")
        saverecord.save()
    else:
        return HttpResponse("failed")
    return redirect('customer')
    
#redirect the pages into the given html files (line 89-100)
def counter(request):
     return render(request,'admincounter.html')

def reader(request):
    return render(request,'adminmeterreader.html')

def customer(request):
    showall=Customers.objects.all()
    return render(request,'admincustomer.html',{"data":showall})

def admain(request):   
    rev = Revenue.objects.all()
    data = [["Amount","Date"]]
    for revs in rev:
        data.append([str(revs.date),revs.amount])
    modified_data = json.dumps(data)
    return render(request,'admin.html',{'data':modified_data})

def addmeterreader(request):
    if request.method == 'POST':
        cust = Users.objects.all()
            
        emails = request.POST.get('email')
        email= emails.lower()
        citizenships = request.POST.get('citizenship')
        citizenship=citizenships.lower()         
        if cust.filter(email=email).exists() or cust.filter(citizenship=citizenship).exists():
            print('email taken')
            
            return redirect('addmeterreader')
        else:
            saverecord = Users(email=email,citizenship=citizenship,password="passwords",position="Meterreader")
            saverecord.save()
            print('user created')
            # return HttpResponse("hdsai")
            return redirect('reader')    
    else:
        # return HttpResponse("hdsai")
        return render(request,'addmeterreader.html')

def addcounter(request):
    if request.method == 'POST':
        cust = Users.objects.all()
            
        emails = request.POST.get('email')
        email= emails.lower()
        citizenships = request.POST.get('citizenship')
        citizenship=citizenships.lower()     
                  
        if cust.filter(email=email).exists() or cust.filter(citizenship=citizenship).exists():
            print('email taken')
            
            return redirect('addcounter')
        else:
            saverecord = Users(email=email,citizenship=citizenship,password="passwords",position="Counter")
            saverecord.save()
            print('user created')
            return redirect('counter')    
    else:
        # return HttpResponse("hdsai")
        return render(request,'addcounter.html')

    
def displaycountertable(request):
    showall=Users.objects.filter(position='Counter')
    return render(request,'editcountertabel.html',{"data":showall})

def displayWorkerdata(request,email):
    showall=Users.objects.get(email=email)
    position=showall.position
    # return HttpResponse(showall)
    if position=="Counter":
        return render(request,'editcounter.html',{"data":showall})
    return render(request,'editmeterreader.html',{"data":showall})

def updateWorkerdata(request,email):
    # return HttpResponse("dn")
    updateData=Users.objects.get(email=email)  
    # return HttpResponse(updateData) 
    form=userforms(request.POST,instance=updateData)
    position=updateData.position
    if form.is_valid():
        form.save()
        messages.success(request,'Record successfull')
        if(position=="Counter"):
            return render(request,'editcounter.html',{"data":updateData})
        return render(request,'editmeterreader.html',{"data":updateData})
    else:
        return HttpResponse("failed")

def billrateupdate(request):
    if request.method == 'POST':           
        updateData=Rates.objects.all()  
        # return HttpResponse(updateData)
        rate=request.POST.get('rate')
        fine=request.POST.get('fine')
        discount=request.POST.get('discount')
        # dicts={"id":1,"rate":rate,"fine":fine,"discount":discount}
        saverecord=Rates(id=1,rate=rate,fine=fine,discount=discount)
        saverecord.save()
        return redirect('billrate')

def billrate(request):
        # return HttpResponse("hdsai")
        data=Rates.objects.all()
        return render(request,'billrate.html',{"data":data})
    


