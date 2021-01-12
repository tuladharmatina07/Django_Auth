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
        return redirect('/')

    return render(request, 'registration.html', {'fm': fm})

# def update(request):
#     if request.method == "POST":
#         u_fm = UpdateForm(data= request.POST, instance=request.user)
#         if u_fm.is_valid():
#             u_fm.save()
#             message.success(request, "Profile updated")
#         else:
#              u_fm = UpdateForm(instance=request.user)
#     return render(request,'update-profile.html', {'u_fm': u_fm})
