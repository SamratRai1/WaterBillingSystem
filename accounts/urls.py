from django.urls import path
from accounts import views
# from admin.views import admain
from admin import views as sa
urlpatterns = [
    path('', views.login, name ='login'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('admain', sa.admain, name='admain')

]
