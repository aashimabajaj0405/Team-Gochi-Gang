from django.shortcuts import render

import cloudinary
import cloudinary.uploader
# Create your views here.
def uploadFile(file):
    resp = cloudinary.uploader.upload(file)
    return resp['url']


def home(request):
    context = {
        
    }
    return render(request,'index.html',context)

def contact(request):
    context = {
        
    }
    return render(request,'contact.html',context)

def maps(request):
    context = {
        
    }
    return render(request,'maps.html',context)