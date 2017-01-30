from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic


from blog.models import Blog
from .models import Project


# Create your views here.


def index(request):
    return render(request, "mainsite/index.html", { "blogs": Blog.objects.all().order_by("-date_create")[0:6] , 'projects': Project.objects.all() })

def about(request):
    return HttpResponse("This is the about page")

class Project_List_View(generic.ListView):
    context_object_name = "portfolio_projects"
