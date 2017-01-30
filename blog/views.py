from django.views import generic

from .models import Blog

class IndexView(generic.ListView):
    context_object_name = 'blog_post_list'

    def get_queryset(self):
        return  Blog.objects.order_by('-date_create')

class  PostView(generic.DetailView):
    model = Blog





