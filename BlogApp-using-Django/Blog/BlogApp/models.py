from django.db import models

# Create your models here.

class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    blog_title = models.CharField(max_length=50)
    content = models.TextField()
    post_date = models.DateField()
    username = models.CharField(max_length=50)

    def __str__(self):
        return self.blog_title


class Author(models.Model):
    about = models.TextField()
    authorname =  models.CharField(max_length=50)

    def __str__(self):
        return self.authorname