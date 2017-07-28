from django.views import generic

from .models import Blog

class IndexView(generic.ListView):
    context_object_name = 'blog_post_list'

    def get_queryset(self):
        return  Blog.objects.filter(publish=True).order_by('-date_created')

class  PostView(generic.DetailView):
    model = Blog





