from django.db import models
from datetime import date
from podcast_user.models import PodcastUser

class Podcast_Blog(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500, default="Post something!! (xc")
    date_of_blog = models.DateField(default=date.today)
    blog_text = models.TextField(default="Must be something")
    blog_user = models.ForeignKey(PodcastUser,on_delete=models.CASCADE,blank=False, null=False)

    def __str__(self):
        return f"{self.id} , {self.name}, {self.blog_user} "

