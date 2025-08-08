from django.shortcuts import render

def home_view(request):
    return render(request, 'main/index.html')

def pampers_view(request):
    return render(request, 'main/pampers.html')

def boys_view(request):
    return render(request, 'main/boys.html')

def girls_view(request):
    return render(request, 'main/girls.html')

def soap_view(request):
    return render(request, 'main/soap.html')

def stroller_view(request):
    return render(request, 'main/stroller.html')

def bottle_view(request):
    return render(request, 'main/bottle.html')

def offers_view(request):
    return render(request, 'main/offers.html')

def about_view(request):
    return render(request, 'main/about.html')

def contacts_view(request):
    return render(request, 'main/contacts.html')

def cart_view(request):
    return render(request, 'main/cart.html')

def login_view(request):
    return render(request, 'main/login.html')
