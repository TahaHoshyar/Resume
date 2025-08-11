from django.urls import path
from resumeapp.views import *
app_name = 'resumeapp'
urlpatterns = [
    #path('url address' , 'view')
    path('', index_view , name= 'index'),
    #path('about' , about_view),
    #path('contact' , contact_view)
]
