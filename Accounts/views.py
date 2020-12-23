from django.shortcuts import render
from .forms import RegistrationForm
from django.contrib import messages

# Create your views here.

def registration(request):
    fm= RegistrationForm()
    if request.method == "POST":
        fm = RegistrationForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,
            'Registration Created Successfully')

        else:
            fm = RegistrationForm()
        
    return render(request, 'registration.html', {'fm': fm})

