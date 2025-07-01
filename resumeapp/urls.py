from django.urls import path
from resumeapp.views import *
urlpatterns = [
    #path('url address' , 'view')
    path('', index_view),
    path('about' , about_view),
    path('contact' , contact_view)
]
