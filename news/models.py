from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField()
    link = models.URLField()
    image = models.URLField()
    post_name = models.CharField(max_length=100)
    guid = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return F"{self.post_name}: {self.title}"