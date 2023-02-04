from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    preamble = models.CharField(max_length=100000, verbose_name='Preamble')
    body = models.TextField(blank=True, null=True, verbose_name='Body')
    body_as_markdown = models.BooleanField(default=False,verbose_name='As markdown')
    created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Created')
    updated = models.DateTimeField(auto_now=True, editable=False, verbose_name='Updated')
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.pk} {self.title}'

    def delete(self, *args):
        self.deleted = True
        self.save()