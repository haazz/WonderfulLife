from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True)

    def get_absolute_url(self):
        return f'/meditation/category/{self.slug}'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class YoutubePost(models.Model):
    title = models.CharField(max_length=50)
    link = models.TextField()
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'[{self.pk}]{self.title} - {self.category}'
    def get_youtube_url(self):
        return self.link

    def get_thumbnail_url(self):
        link_split = self.link.split('/')
        return "https://img.youtube.com/vi/" + link_split[-1] + "/0.jpg"
