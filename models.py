from django.db import models
from django.forms import ModelForm
from django.utils import timezone

class Author(models.Model):
    NATION_CHOICES = (
        ('CH', 'China'),
        ('US', 'America'),
        ('UK', 'England'),
        ('GE', 'German'),
        ('CA', 'Canada'),
    )
    name = models.CharField(max_length=80, unique=False, verbose_name='Author name')
    nation = models.CharField(max_length=80, unique=False, verbose_name='Nationality', choices=NATION_CHOICES)
    
    def save(self, *args, **kwargs):
        try:
            old_author = Author.objects.get(name=self.name)
        except Author.DoesNotExist:
            super().save(*args, **kwargs)
            return self        
        else:
            return old_author
            
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

class AuthorForm(ModelForm):        
    class Meta:
        model = Author
        fields = '__all__'
        
class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'pub_date', 'context']