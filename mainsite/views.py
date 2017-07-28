from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import Link
from blog.models import Blog
from projects.models import Project


# Create your views here.


def index(request):
    return render(request, "mainsite/index.html",
    {
    "blogs": Blog.objects.all().order_by("-date_created")[0:6]
    , 'projects': Project.objects.all()
    })

def about(request):
    resume = Link.objects.filter(name='*')
    resume = resume[0]
    return render(request, "mainsite/about.html", { 'link': resume})

class Project_List_View(generic.ListView):
    context_object_name = "portfolio_projects"
