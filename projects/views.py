from django.views import generic

from .models import Project


# Create your views here.


class IndexView(generic.ListView):
    context_object_name = 'projects_list'

    def get_queryset(self):
        return Project.objects.all()

class PostView(generic.DetailView):
    model = Project

