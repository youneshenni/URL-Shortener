from django.shortcuts import render
from .models import MiniURL
from .forms import MiniURLForm
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .functions import hash
from django.http import HttpResponseRedirect

# Create your views here.
#Redirection view
def redirect(request, arg):
    return HttpResponseRedirect(get_object_or_404(MiniURL, code=request.build_absolute_uri()).LongURL)
#Main View that displays the page
def Hello(request):
    hello = reverse(Hello)
    formular = MiniURLForm
    form = MiniURLForm(request.POST or None)
    redir = request.build_absolute_uri()
    #Get data from Model
    entries = MiniURL.objects.all()
    #We need to display the three fields
    Container = list()
    for entry in entries:
        Container.append({'long':entry.LongURL, 'short':entry.code, 'date':entry.date})
    #Handle Form
    #Check if valid
    if form.is_valid():
        #Put Long URL into url variable 
        url = form.cleaned_data["LongURL"]
        #Create shortened URL
        hash(url, redir)

    return render(request, "mini_url/base.html", locals())