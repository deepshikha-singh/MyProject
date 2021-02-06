from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    context = {'name': 'Army', 'course': 'Django'}
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def project(request):
    return render(request, 'project.html')

def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        textarea = request.POST['textarea']
        #print("name,email,phone,textarea")
        ins = Contact(name=name, email=email, phone=phone, textarea=textarea)
        ins.save()  
        print("The data has been written to the db")

    return render(request, 'contact.html')