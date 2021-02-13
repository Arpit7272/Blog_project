from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

#class for Post 
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True,null=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

#Method to publish the content
    def publish(self):
        self.publish_date = timezone.now()
        self.save()
 # select the approved comments for adding to Post   
    def approved_comments(self):
        return self.comments.filter(approved_comments=True)
# Method for viewing
    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk})
    def __str__(self):
        return self.title


#class to post comment
class Comment(models.Model):
    post= models.ForeignKey('blog.Post',related_name='comments',on_delete= models.CASCADE)
    author= models.CharField(max_length=100)
    text= models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    approved_comments = models.BooleanField(default=False)

# Method to approve comments to Post
    def approve(self):
        self.approved_comments = True
        self.save()
    
# view call
    def get_absolute_url(self):
        return reverse('post_list')


    def __str__(self):
        return self.text


