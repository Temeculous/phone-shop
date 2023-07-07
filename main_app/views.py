from django.shortcuts import render

# Importing the phone model so we have acces to the class
from .models import Phone           

# Create your views here.
def home(request):
    return render(request, 'home.html')


# Accesses all the attributes of the phone class and passes the data down
# to the index.html
def phones_index(request):
    phones = Phone.objects.all()
    return render(request, 'phones/index.html', {
        'phones': phones
    })