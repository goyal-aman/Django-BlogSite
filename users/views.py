from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            #saving user: form.save()
            form.save() 
            username = form.cleaned_data.get('username')
            messages.success(request, 'Successfully Registered')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})