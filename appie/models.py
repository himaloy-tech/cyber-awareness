from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.TextField()
    message = models.TextField()
    email = models.EmailField()
    datetime = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    def __str__(self):
        return f"{self.name}"

class Article(models.Model):
    thumbnail = models.ImageField(upload_to='thumbnails')
    title = models.TextField(default="")
    desc = models.TextField()
    id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.title}"


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    def __str__(self):
        return f"{self.time}"
    
    def serialize(self):
        context = {
            "comment" : self.comment,
            "time" : self.time
        }
        return context