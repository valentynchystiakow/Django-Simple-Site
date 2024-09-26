# import libraries(modules)
from django.db import models


# Sql models


# Articles sql mode
class Articles(models.Model):
    # model poles with their types
    title = models.CharField('Article title', max_length=50)
    announcement = models.CharField('Article announcement', max_length=250)
    full_text = models.TextField('Article text')
    date = models.DateTimeField('Publication date')

    # represents model in string type
    def __str__(self):
        return f'New: {self.title}'

    # redirects user to detail new after deleting/updating it
    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
