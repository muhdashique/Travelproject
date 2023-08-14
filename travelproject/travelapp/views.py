from django. http import HttpResponse
from django.shortcuts import render
from .models import place,teacher

# Create your views here.
from django. http import HttpResponse
from django.shortcuts import render
def home(request):
    obj=place.objects.all()
    data=teacher.objects.all()


    return render(request,"index.html",{'result':obj,'obj':data})





