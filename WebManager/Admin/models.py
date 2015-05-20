from django.db import models
from django.contrib.auth.models import User
from encrypted_fields import EncryptedTextField

# Create your models here.
class Site(models.Model):
    name = models.CharField(max_length=128, unique=True)
    type = models.CharField(max_length=64)
    niche = models.TextField()
    notes = models.TextField()
    user = models.CharField(max_length=64)
    pw = EncryptedTextField()
    
    def __str__(self):
        return self.name
    

class Keyword(models.Model):
    word = models.CharField(max_length=2048, unique=True)
    ems = models.IntegerField()
    cpc = models.FloatField()
    difficulty = models.FloatField()
    discarded = models.BooleanField(default=False)
    
    def __str__(self):
        return self.word
    

class Article(models.Model):
    title = models.CharField(max_length=1024)
    site = models.ForeignKey("Site", blank=True, null=True)
    posted = models.BooleanField(default=False)
    text = models.TextField()
    author = models.ForeignKey("Employee")
    date = models.DateField(auto_now_add=True)
    keywords = models.ManyToManyField("Keyword", null=True, blank=True)
    
    def __str__(self):
        return self.title
    
class Employee(models.Model):
    user = models.OneToOneField(User)
    trust = models.IntegerField(default=0)
    salary = models.FloatField()
    type = models.TextField()
    
    def __unicode__(self):
        return self.user.username
    
    def __str__(self):
        return self.name
    

class EmployeeHash(models.Model):
    hash = models.CharField(max_length=16)
    trust = models.IntegerField(default=0)
    name = models.TextField()
    surname = models.TextField()
    type = models.TextField()
    
    
class Job(models.Model):
    name = models.CharField(max_length=128)
    taker = models.ForeignKey("Employee", null=True, blank=True)
    posted = models.DateTimeField(auto_now_add=True)
    taken = models.DateTimeField(null=True, blank=True)
    type = models.CharField(max_length=64)
    keywords = models.ManyToManyField("Keyword", null=True, blank=True)
    description = models.TextField()
    flags = models.CharField(max_length=64)
    
    def __str__(self):
        return self.name
    
    
class Campaign(models.Model):
    type = models.CharField(max_length=128)
    notes = models.TextField()
    site = models.ForeignKey("Site")
    started = models.DateTimeField()
    

class CampaignData(models.Model):
    campaign = models.ForeignKey("Campaign")
    name = models.TextField()
    data = models.TextField()
    
    
    
    
    