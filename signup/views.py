from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from bs4 import BeautifulSoup

with open("C:/Users/HP/Desktop/Reg Form/main/templates/signup.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')


def signup(request):
    
    if request.method == 'POST':
        # Get form values
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['pass']
        re_pass = request.POST['re_pass']
       
        # Check if passwords match
        if password == re_pass:
            # Check email
            if User.objects.filter(email=email).exists():
                messages.error(request,'Email already exists.')
                return redirect('signup')
            else:
                if soup.find_all("input", class_="checked"):
                    user = User.objects.create_user(username=name,email=email,password=password)
                    user.save()
                    messages.success(request,'Sign up successful.')
                    return redirect('login')
                else:    
                    messages.error(request,'You must agree with the terms of service.')
                    return redirect('signup')
        else:
            messages.error(request,'Passwords must match.')
            return redirect('signup')

    return render(request,'signup.html')
