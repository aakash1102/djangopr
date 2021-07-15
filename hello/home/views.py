from django.shortcuts import render 
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'index.html')

def register(request):
    return render(request,'/templates/register.html')


'''def services(request):
    return HttpResponse("this is service page''''''  !!")

def contact(request):
    return HttpResponse("this is contact..... page.......  !!")'''