from django.shortcuts import render
from .models import MiniURL
from .forms import MiniURLForm
from django.urls import reverse
from django.shortcuts import get_object_or_404
# Create your views here.
#Redirection view
def Redirect(url):
    get_object_or_404(MiniURL, LongURL=url)
#Main View that displays the page
def Hello(request):
    hello = reverse(Hello)
    formular = MiniURLForm
    form = MiniURLForm(request.POST or None)
    #Get data from Model
    entries = MiniURL.objects.all()
    #We need to display the three fields
    Long, short, date = list(), list(), list()
    for entry in entries:
        Long.append(entry.LongURL)
        short.append(entry.code)
        date.append(entry.date)
    #Handle Form
    #Check if valid
    if form.is_valid():
        #Put Long URL into url variable 
        url = form.cleaned_data["LongURL"]
        #Create shortened URL

        #Add to model

    return render(request, "mini_url/base.html", locals())