from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html')
    
def registration(request):
    fm= RegistrationForm()
    if request.method == "POST":
        fm = RegistrationForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,
            'Registration Created Successfully')
        return redirect('Login')

    return render(request, 'registration.html', {'fm': fm})

