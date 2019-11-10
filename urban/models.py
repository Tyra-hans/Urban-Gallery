from django.db import models
import datetime as dt

class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['first_name']

    def save_editor(self):
        self.save()

class Location(models.Model):
    name = models.CharField(max_length =30)
  
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length =60)
    post = models.TextField()
    editor = models.ForeignKey(Editor)
    tags = models.ManyToManyField(tags)
    location = models.ForeignKey(Location)
    pub_date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def todays_photos(cls):
        today = dt.date.today()
        image = cls.objects.filter(pub_date__date = today)
        return image

    @classmethod
    def days_photos(cls,date):
        images = cls.objects.filter(pub_date__date = date)
        return images