from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from accounts.models import Users
from accounts.models import Customers
from accounts.models import Rates
from meterreader.forms import customerforms
from django.contrib import messages
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
# Create your views here.
def meterreaderhome(request):
    if request.method == "POST":
        # return HttpResponse("....")
        meternum=int(request.POST.get('meternum'))
        lastestunit=int(request.POST.get('latestunit'))
       
        try:
            cust=Customers.objects.get(meternum=meternum)
            
            previousunit=int(cust.currentunit)
            
            rates=Rates.objects.get(pk=1)
            fineamount=0      
            if previousunit<lastestunit and cust.status==True:
                
                currentunit=lastestunit-previousunit
                
                if(int(cust.totaldue)!=0):              
                    fineamount=round(((int(rates.fine))/100 * (currentunit*(int(rates.rate)))))               
                    totaldue=int(cust.totaldue)+(currentunit*(int(rates.rate)))+fineamount
                else:
                    
                    totaldue=int(cust.totaldue) + currentunit*(int(rates.rate))
                # return HttpResponse(fineamount)    
                thisdict={"customername":cust.customername,"email":cust.email,"citizenship":cust.citizenship,"address":cust.address,"password":cust.password,"status":cust.status,"currentunit":lastestunit,"discountamount": 0 ,"fineamount":fineamount,"previousunit":cust.currentunit,"totaldue":totaldue,"meternum":cust.meternum}
                previousdue=cust.totaldue
                form=customerforms(thisdict,instance=cust)
                # return HttpResponse(form)
                if form.is_valid():
                    buf = io.BytesIO()
                    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
                    textob = c.beginText()
                    textob.setTextOrigin(inch,inch)
                    textob.setFont('Helvetica',14)
                    lines= []
                    
                    
                    lines.append("Customer name = "+str(cust.customername))
                    
                    lines.append("Customer email = "+str(cust.email))
                    
                    lines.append("Customer citizenship = "+str(cust.citizenship))
                    
                    lines.append("Address = "+str(cust.address))
                    lines.append("Meter number = "+str(cust.meternum))
                    lines.append("Current meter unit = "+str(lastestunit))
                    lines.append("Previous meter unit = "+str(previousunit))
                    lines.append("Previous due = "+str(previousdue))
                    lines.append("Fine amount = "+str(cust.fineamount))
                    lines.append("Totaldue = "+str(totaldue))
                    # return HttpResponse(lines)
                    for line in lines:
                        textob.textLine(line)
                    # return HttpResponse(cust.totaldue)
                    c.drawText(textob)
                    c.showPage()
                    c.save()
                    buf.seek(0)
                    form.save()
                    file=str(cust.meternum)+".pdf"
                    return FileResponse(buf, as_attachment=True, filename=file)
                else:
                    # return HttpResponse("failed")
                    messages.success(request,"Adding meter unit failed")
            else:
                
                if previousunit > lastestunit:
                    messages.success(request,"Latest unit should be greater than previous unit")
                if cust.status== False:
                    messages.success(request,"User is inactive")
            return render(request,'meterreaderhome.html')    
        except:
            # return HttpResponse("except")
            messages.success(request,"Meter number does not exist")
            
            return render(request,"meterreaderhome.html")
    else:
        return render(request,'meterreaderhome.html')
        
    

def changepass(request,email):
    showall = Users.objects.get(email=email)
    return HttpResponse(showall)
    if request.method == 'post':
        pass
    else:
        return render(request,'changepass.html')
   