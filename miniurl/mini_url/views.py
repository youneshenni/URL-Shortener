from django.shortcuts import render
from .models import MiniURL
from .forms import MiniURLForm
from django.urls import reverse
# Create your views here.
def Hello(request):
    hello = reverse(Hello)
    formular = MiniURLForm
    form = MiniURLForm(request.POST or None)
    #Get data from Model
    
    #Handle Form
    #Check if valid
    if form.is_valid():
        #Put Long URL into url variable 
        url = form.cleaned_data["LongURL"]
        #Create shortened URL

        #Add to model

    return render(request, "mini_url/base.html", locals())