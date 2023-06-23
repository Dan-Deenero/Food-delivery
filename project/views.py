from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'project/home.html')

def contact(request):
    return render(request, 'project/contact.html')


def dishes(request):
    return render(request, 'project/dishes.html')

def menu(request):
    return render(request, 'project/menu.html')

def cart(request):
    return render(request, 'project/cart.html')

def update_profile(request):
    return render(request, 'project/edit-profile.html')
