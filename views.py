from django.shortcuts import render
from django.views import generic
from .models import Article

# Create your views here.
class IndexView(generic.ListView):
    template_name = "blogsgn/index.html"
    context_object_name = 'entry_list'
    
    def get_queryset(self):
        return Article.objects.order_by('-pub_date')
        
        
class ArticleView(generic.DetailView):
    model = Article
    context_object_name = 'article'
    template_name = "blogsgn/detail.html"