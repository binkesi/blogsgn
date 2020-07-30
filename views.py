from django.shortcuts import render
from django.views import generic
from .models import Article, Comments, CommentsForm, ArticleForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
class IndexView(generic.ListView):
    template_name = "blogsgn/index.html"
    context_object_name = 'entry_list'
    
    def get_queryset(self):
        return Article.objects.order_by('-pub_date')[:5]
        
        
#class ArticleView(generic.DetailView):
#    model = Article
#    context_object_name = 'article'
#    template_name = "blogsgn/detail.html"
    
def get_comment(request, pk):
    template_name = 'blogsgn/detail.html'
    #context_object_name = 'article'
    article = get_object_or_404(Article, pk=pk)
    comments = article.comments_set.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentsForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.article = article
            # Save the comment to the database
            new_comment.save()
            comment_form = CommentsForm()
    else:
        comment_form = CommentsForm()

    return render(request, template_name, {'article': article,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})
                                           
def new_article(request):
    template_name = 'blogsgn/new.html'
    new_article_form = None
    if request.method == 'POST':
        new_article_form = ArticleForm(data=request.POST)
        if new_article_form.is_valid():
            article = new_article_form.save()
        return HttpResponseRedirect(reverse('blogsgn:detail', args=(article.id,)))
            
    else:
        new_article_form = ArticleForm()
        return render(request, template_name, {'new_article_form': new_article_form})