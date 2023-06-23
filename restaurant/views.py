from django.shortcuts import render

# Create your views here.
def viewDish(request):
    return render(request, 'restaurant/viewFood.html')
