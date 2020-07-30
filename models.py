from django.db import models
from django.forms import ModelForm
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=80, unique=True, verbose_name='Author name')
    nation = models.CharField(max_length=80, unique=False, verbose_name='Nationality')
    
    def __str__(self):
        return self.name

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=80, unique=True, verbose_name='Article name')
    pub_date = models.DateTimeField('date published')
    author = models.ForeignKey(Author, null=True, on_delete=models.CASCADE)
    context = models.TextField()
    
    def __str__(self):
        return self.title
        
class Comments(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    name = models.CharField(max_length=80, null=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)  
    
class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['name', 'body', 'active']
        
class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'