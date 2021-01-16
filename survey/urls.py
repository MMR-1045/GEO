from django.urls import path
from .import views

app_name='survey'

urlpatterns = [
    #leave as empty string for base url
    path('',views.survey,name='survey'),
    
]