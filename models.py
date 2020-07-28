from django.db import models

# Create your models here.
class EntryArticle(models.Model):
    name = models.CharField(max_length=80, unique=True, verbose_name='Article name')
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.name