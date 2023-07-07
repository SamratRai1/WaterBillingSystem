from django.urls import  path
from customer import views
urlpatterns = [
    path('',views.changepass,name='changepass'),
    # path('addmeter',views.addmeter,name='addmeter'),
    
]