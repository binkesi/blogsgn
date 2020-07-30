from django.shortcuts import render
from django.views import generic
from .models import Article, Comments, CommentsForm
from django.shortcuts import render, get_object_or_404

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