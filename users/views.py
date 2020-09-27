from django.contrib.auth import login , authenticate , logout
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import CustomUserCreationForm



def dashboard(request):
    return render(request, "users/dashboard.html")

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=raw_password , email=email)
            login(request, user)
            return redirect('users:')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})
