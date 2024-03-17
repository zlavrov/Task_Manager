from django.db import models

class Task(models.Model):

    title = models.CharField('Title', max_length = 50)
    content = models.TextField('Content')
    createdAt = models.DateTimeField('CreatedAt', auto_now = True)
    updatedAt = models.DateTimeField('UpdatedAt', auto_now_add = True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'A task'
        verbose_name_plural = 'Tasks'
