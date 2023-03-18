from django.shortcuts import render,redirect
from django.contrib import messages,auth

def login(request):
    # messages.error(request,'Works!')
    if request.method == 'POST':
        # Get form values
        name = request.POST['your_name']
        password = request.POST['your_pass']

        user = auth.authenticate(username=name, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, f'Welcome {user.username}')
            messages.success(request, 'You have successfully logged in!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials.')
            return redirect('login')
    return render(request,'login.html')

def dashboard(request):
    return render(request,'dashboard.html')
