from django.db import models
from datetime import date,datetime
from podcast_user.models import PodcastUser

class Podcast_Blog(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500, default="Post something!! (xc")
    time_of_blog = models.DateTimeField(default=datetime.now)
    blog_text = models.TextField(default="Must be something")
    blog_user = models.ForeignKey(PodcastUser,on_delete=models.CASCADE,blank=False, null=False)

    def __str__(self):
        return f"{self.id} , {self.name}, {self.blog_user} "


class BlogComment(models.Model):
    id = models.AutoField(primary_key=True)
    blog = models.ForeignKey(Podcast_Blog, on_delete=models.CASCADE, related_name='comments')
    comment_text = models.TextField()
    comment_user = models.ForeignKey(PodcastUser, on_delete=models.CASCADE, blank=False, null=False)
    time_of_comment = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.id}, {self.comment_text}, {self.comment_user}"