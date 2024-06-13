from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_backends
from django.contrib import messages
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib.auth.decorators import login_required
from .models import Profile

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Specify the backend
            backend = get_backends()[0]
            user.backend = f"{backend.__module__}.{backend.__class__.__name__}"
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('index')  # Redirect to a home page or another appropriate page
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Replace 'home' with your desired URL name
        else:
            error_message = "Invalid credentials"
    else:
        error_message = None
    return render(request, 'login.html', {'error_message': error_message})
# Create your views here.


@login_required
def index(request):
    
    return render(request, 'index.html')


@login_required
def profile_view(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile, initial={'username': user.username, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email})
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile, initial={'username': user.username, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email})
    return render(request, 'profile_form.html', {'form': form})

@login_required
def profile_page(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    return render(request, 'profile.html', {'user': user, 'profile': profile})