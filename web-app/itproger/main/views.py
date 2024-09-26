# import libraries
from django.shortcuts import render


# views
# main page view
def index(request):
    return render(request, 'main/index.html',)


# about page view
def about(request):
    return render(request, 'main/about.html')


# contacts page view
def contacts(request):
    return render(request, 'main/contacts.html')
