from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from simpleapp.models import Blog


class HomeView(TemplateView):
    template_name = "simpleapp/index.html"


class BlogView(ListView):
    template_name = "simpleapp/blog.html"
    queryset = Blog.objects.all()
    context_object_name = "blogs"
