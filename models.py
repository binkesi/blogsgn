from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=80, unique=True, verbose_name='Author name')
    nation = models.CharField(max_length=80, unique=False, verbose_name='Nationality')
    
    def __str__(self):
        return self.name

# Create your models here.
class EntryArticle(models.Model):
    name = models.CharField(max_length=80, unique=True, verbose_name='Article name')
    pub_date = models.DateTimeField('date published')
    author = models.ForeignKey(Author, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name