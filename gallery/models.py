from django.db import models

class Photo(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='gallery')
    alt = models.TextField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        ordering = ['name']

class Gallery(models.Model):
    name = models.CharField(max_length=250)
    images = models.ManyToManyField(Photo)
    alt = models.TextField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Галлерея'
        verbose_name_plural = 'Галлереи'
        ordering = ['name']
