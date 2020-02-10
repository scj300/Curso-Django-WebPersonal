from django.db import models

# Create your models here.
# class that represent a table in the Data Base
class Project(models.Model):

    title = models.CharField(max_length=200, verbose_name='Title')
    description = models.TextField()
    image = models.ImageField(upload_to='projects')
    link = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        '''
        Add new config parameters
        '''
        verbose_name = 'second name'
        verbose_name_plural = 'projects'
        ordering = ['-created'] # '-' delante de la ordenación para que sea del revés

    def __str__(self):
        return self.title
