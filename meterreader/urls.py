from django.urls import  path
from meterreader import views
urlpatterns = [
    path('',views.meterreaderhome,name='meterreaderhome'),
    # path('addmeter',views.addmeter,name='addmeter'),
    
]