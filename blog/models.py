from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
#Databse creation 

class Post(models.Model):
	title=models.CharField(max_length=100)
	content=models.TextField()
	date_posted=models.DateTimeField(default=timezone.now)
	author=models.ForeignKey(User, on_delete=models.CASCADE)
	post_img_url = models.URLField(max_length=300, blank=True, null=True)
	
	def __str__(self):
		return self.title
		
	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})
		
##Recent posts

class PostManager(models.Manager):
    def recent_posts(self, limit=5):
        return self.filter(date_posted__lte=timezone.now()).order_by('date_posted')[:limit]
	
