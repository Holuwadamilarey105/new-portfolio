from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages

def index(request):
    return render(request, "index.html")

def submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Save to database
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        messages.success(request, 'Your message has been submitted successfully!')
        
    return redirect('/')