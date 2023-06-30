from django.shortcuts import render, redirect
from item.models import Category, Item
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def index(request):

    categories = Category.objects.all()
    categoryID = request.GET.get('category')
    
    if categoryID:
        items = Item.objects.filter(is_sold=False,category=categoryID).all()
    else:
            items = Item.objects.filter(is_sold=False).all()
    return render(request,'index.html',{
        'categories' : categories,
        'items' : items,
        'categoryID' : categoryID
    })

def contact(request):
    return render(request,'contact.html')

def signup(request):
    
    if request.method == 'POST':
        un = request.POST['username']
        em = request.POST.get('email')
        fn = request.POST.get('fname')
        ln = request.POST.get('lname')
        pw = request.POST.get('pass1')
        cpw = request.POST.get('pass2')
        

        if User.objects.filter(username=un).exists():
            messages.info(request,"Username is already exist")
                
        else:
            user = User.objects.create_user(username= un,email=em,password=pw)
            user.first_name = fn
            user.last_name = ln
        
            user.save()
                
            messages.success(request,'Your account has been created successfully')
                    
            return redirect('core:signin')
            
            
        
    return render(request,'signup.html')   


def signin(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass1')
        
        user = authenticate(username=username,password=password)
        
        if user is not None:
            fn = user.first_name
            login(request,user)
            messages.success(request,"You are signed in successfully")
            
            return render(request,'index.html',{
                'fn' : fn
            })
            
        else:
            messages.error(request,'Credentials do not match')    
            return redirect('core:index')
        
    return render(request,'signin.html')

def signout(request):
    logout(request)
    messages.success(request,"You are signed out successfully")
    
    return redirect('core:index')