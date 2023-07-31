from django.db import models

class Articles(models.Model):
   title = models.CharField('Name', max_length=50, default="")
   announcement = models.CharField('Announcement', max_length=250, default="")
   fullText = models.TextField('Article', max_length=50, default="")
   date = models.DateTimeField('Date', max_length=500, default="")
   
   def __str__(self):
      return self.title
   
   class Meta:
      verbose_name = 'Article'
      verbose_name_plural = "Articles"
   
