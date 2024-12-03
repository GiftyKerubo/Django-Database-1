from django.shortcuts import render,get_object_or_404
from .models import Blogpost

# Create your views here.

def blog_list(request):
    posts=Blogpost.objects.all()
    # it retrieves everything from the database
    return render(request,'blog_list.html',{'posts':posts})
def blog_detail(request):
    post=get_object_or_404(Blogpost,id=id)
    return render(request,'blog_details.html',{'post':post})
