from django.db import models
from django.contrib.auth.models import User
from thumbs import ImageWithThumbsField
from apps.projects.models import Project


class News(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField()
    image = ImageWithThumbsField(null=True, blank=True, upload_to='images/news', sizes=((300, 300), (90, 90), ))
    author = models.ForeignKey(User)
    datetime = models.DateTimeField()
    projects_relateds = models.ManyToManyField(Project, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'News'

    def __unicode__(self):
        return self.title
