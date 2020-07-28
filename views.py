from django.shortcuts import render
from django.views import generic
from .models import EntryArticle

# Create your views here.
class IndexView(generic.ListView):
    template_name = "blogsgn/index.html"
    context_object_name = 'article_list'
    
    def get_queryset(self):
        return EntryArticle.objects.all()