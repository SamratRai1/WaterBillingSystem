from unicodedata import name
from django.urls import path
from admin import views
urlpatterns = [
    #path('', views.adminhome, name='adminhome'),
    #path('counter/registercounter', views.registercounter, name='registercounter'),
    
    path('activateusers/<str:email>',views.activateusers,name='activateusers'),
    path('registermeter', views.registerWorkers, name='registermeter'),
    path('displaycounter', views.displayWorker, name='displaycounter'),
    path('registerworkers/<str:position>', views.registerWorkers,name='registerworkers'),
    path('displayworker/<str:position>', views.displayWorker,name='displayworker'),
    path('editworker', views.displayWorker,name='editworker'),
    path('displayWorkerdata/updateWorker/<str:email>/<str:position>', views.updateWorker,name='updateWorker'),
    path('counter',views.counter,name='counter'),
    path('reader',views.reader,name='reader'),
    path('customer',views.customer,name='customer'),
    path('admain',views.admain,name='admain'),
    path('deleteusers/<str:email>',views.deleteusers,name='deleteusers'),
    path('addmeterreader',views.addmeterreader,name='addmeterreader'),
    path('displaymeterreader',views.displaymeterreader,name='displaymeterreader'),
    path('addcounter',views.addcounter,name='addcounter'),
    path('displaycountertable',views.displaycountertable, name='displaycountertable'),
    path('displayWorkerdata/updateWorkerdata/<str:email>',views.updateWorkerdata,name='updateWorkerdata'),
    path('displayWorkerdata/<str:email>', views.displayWorkerdata,name='displayWorkerdata'),
    path('billrate',views.billrate,name="billrate"),
    path('billrateupdate',views.billrateupdate,name="billrateupdate")
       
]
