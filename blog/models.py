from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField(auto_now=False)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title
