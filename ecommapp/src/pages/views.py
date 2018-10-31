from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404

from .forms import ContactForm

def home_page(request):
    context = {
        "title": "Home",
        "content": "Welcome to the Home Page.",
    }
    if request.user.is_authenticated:
        context["premium_content"] = "YEAHHHH!"
    
    return render(request, 'home_page.html', context)
    
def about_page(request):
    context = {
        "title": "About",
        "content": "Welcome to the About Page.",
    }
    return render(request, 'home_page.html',context)

def contact_page(request):

    contact_form = ContactForm(request.POST or None)
    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    context = {
        "title": "Contact",
        "content": "Welcome to the Contact Page.",
        "form": contact_form,
    }
    # if request.method=='POST':
    #     print(request.POST)
    #     print(request.POST.get('full_name'))
    
    return render(request, 'contact/view.html',context)

