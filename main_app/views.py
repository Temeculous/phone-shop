from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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

# Find's phone by id and returns a page containing more info on that phone object
def phone_detail(request, phone_id):
    phone = Phone.objects.get(id=phone_id)
    return render(request, 'phones/detail.html', {'phone': phone})

class PhoneCreate(CreateView):
    model = Phone
    fields = '__all__'

class PhoneUpdate(UpdateView):
    model = Phone
    fields = ['make', 'serial', 'color', 'condition']

class PhoneDelete(DeleteView):
    model = Phone
    success_url = '/phones'