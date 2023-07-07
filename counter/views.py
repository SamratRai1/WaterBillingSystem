
from mmap import PAGESIZE
import this
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from accounts.models import Users
from accounts.models import Customers, Revenue
from accounts.models import Rates
from counter.forms import customerforms, revenueforms
from django.contrib import messages
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from datetime import date

# Create your views here.
def counterhome(request):
    if request.method == "POST":
        # return HttpResponse("....")
        meternum=int(request.POST.get('meternum'))
        enteredmoney=int(request.POST.get('enteredmoney'))
       
        try:
            cust=Customers.objects.get(meternum=meternum)
            totaldue=int(cust.totaldue)
            fineamount=int(cust.fineamount)
            rates=Rates.objects.get(pk=1)
            discountrate= int(rates.discount)
            
            discountamount=0
            returnmoney=0
            if enteredmoney<totaldue:
                
                totaldue=totaldue-enteredmoney    
            else:
                if fineamount==0:
                    discountamount=round((discountrate/100)*totaldue)
                totaldue=0
                returnmoney= enteredmoney-cust.totaldue+discountamount        
            thisdict={"customername":cust.customername,"email":cust.email,"citizenship":cust.citizenship,"address":cust.address,"password":cust.password,"status":cust.status,"currentunit":cust.currentunit,"discountamount": discountamount ,"fineamount":cust.fineamount,"previousunit":cust.previousunit,"totaldue":totaldue,"meternum":cust.meternum}
                
            form=customerforms(thisdict,instance=cust)
                # return HttpResponse(form)
            if form.is_valid():
                buf = io.BytesIO()
                c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
                textob = c.beginText()
                textob.setTextOrigin(inch,inch)
                textob.setFont('Helvetica',14)
                lines= []
                
                # datas="Customer name = "+str(cust.customername)+"<br>Customer email = "+str(cust.email)+"<br>Customer citizenship = "+str(cust.citizenship)+"<br>Address = ",str(cust.address)+"<br>Meter number = "+str(cust.meternum)+"<br>Fine amount = "+str(cust.fineamount)+"<br>Discount amount = "+str(discountamount)+"<br>Totaldue = "+str(totaldue)+ "<br>Given money = "+str(enteredmoney)+"<br>Returned money = "+str(returnmoney)
                # 
                
                lines.append("Customer name = "+str(cust.customername))
                
                lines.append("Customer email = "+str(cust.email))
                
                lines.append("Customer citizenship = "+str(cust.citizenship))
                
                lines.append("Address = "+str(cust.address))
                lines.append("Meter number = "+str(cust.meternum))
                lines.append("Fine amount = "+str(cust.fineamount))
                lines.append("Discount amount = "+str(discountamount))
                lines.append("Totaldue = "+str(totaldue))
                lines.append("Given money = "+str(enteredmoney))
                lines.append("Returned money = "+str(returnmoney))
                # return HttpResponse(lines)
                for line in lines:
                    textob.textLine(line)
                # return HttpResponse(cust.totaldue)
                c.drawText(textob)
                c.showPage()
                c.save()
                buf.seek(0)
                todaydate = date.today()
                revs = Revenue.objects.all()
                if revs.filter(date=todaydate).exists():
                    rev = Revenue.objects.get(date=todaydate)
                    totamt = rev.amount + enteredmoney - returnmoney
                    dict = {"date":rev.date,"amount":totamt}
                    forms = revenueforms(dict,instance=rev)
                    if forms.is_valid():
                        forms.save()
                else:
                    totamt = enteredmoney - returnmoney
                    saverecord = Revenue(date=todaydate,amount=totamt)
                    saverecord.save()
                
                form.save()
                # return HttpResponse("dsa")
                return FileResponse(buf, as_attachment=True, filename='receipt.pdf')
                # return HttpResponse("error")
            else:
                    # return HttpResponse("failed")
                messages.success(request,"Payment failed.")
              
        except:
            # return HttpResponse("User does not exist")
            messages.success(request,"Meter number does not exist")
            return render(request,"counterhome.html")
    else:
        
        return render(request,'counterhome.html')

