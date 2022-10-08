from ckeditor.fields import RichTextField
from django.db import models


class ContactModel(models.Model):
    """Класс модели обратной связи"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    message = models.TextField(max_length=5000)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.email}'

    class Meta:
        verbose_name = 'Форма'
        verbose_name_plural = 'Формы'


class ContactLink(models.Model):
    """ Класс модели контаков """
    icon = models.FileField(upload_to='icons/')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class About(models.Model):
    """ Класс страницы модели о нас """
    name = models.CharField(max_length=50, default='')
    text = RichTextField()
    mini_text = RichTextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

    def get_first_image(self):
        item = self.about_images.first()
        return item.image.url

    def get_images(self):
        return self.about_images.order_by('id')[1:]


class ImageAbout(models.Model):
    """ Класс моделей изображений """
    image = models.ImageField(upload_to='about/')
    page = models.ForeignKey(
        About,
        on_delete=models.CASCADE,
        related_name='about_images'
    )
    alt = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class Socials(models.Model):
    """ Класс модели соц. сетей О нас """
    icon = models.FileField(upload_to='icons/')
    name = models.CharField(max_length=200)
    link = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'СоцСеть'
        verbose_name_plural = 'СоцСети'
