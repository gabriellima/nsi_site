from django.db import models
from apps.projects.models import Project


MEMBER_FUNCTIONS = (
    ('gerente', 'gerente'),
    ('coordenador', 'coordenador'),
    ('pesquisador', 'pesquisador'),
    ('bolsista', 'bolsista'),
    ('colaborador', 'colaborador'))


class Participation(models.Model):
    member = models.ForeignKey('Member')
    project = models.ForeignKey(Project)
    start_date = models.DateField()
    end_date = models.DateField(null=True)

class Member(models.Model):
    name = models.CharField(max_length=100)
    currently_does = models.TextField()
    life_and_work = models.TextField()
    function = models.CharField(max_length=100, choices=MEMBER_FUNCTIONS)
    site = models.URLField(null=True, blank=True)
    github = models.CharField(max_length=50, null=True, blank=True)
    twitter = models.CharField(max_length=50, null=True, blank=True)
    slideshare = models.CharField(max_length=50, null=True, blank=True)
    lattes = models.URLField(null=True, blank=True)
    photo = models.ImageField(upload_to='images/members')
    started_nsi_date = models.DateField()
    desertion_nsi_date = models.DateField(null=True, blank=True)
    
    def github_link(self):
        github_site = "http://github.com/"
        return github_site + self.github 
            
    def twitter_link(self):
        twitter_site = "http://twitter.com/"
        return twitter_site + self.twitter 
    
    def slideshare_link(self):
        slideshare_site = "http://www.slideshare.net/"
        return slideshare_site + self.slideshare
