from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    published_date = models.DateField()
    image = models.ImageField(upload_to='books/', null=True, blank=True)

    def __str__(self):
        return self.title
