from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Article(models.Model):
    TYPE = (
        ('tank', 'Танки'),
        ('heal', 'Хилы'),
        ('dd', 'ДД'),
        ('buyers', 'Торговцы'),
        ('gildmaster', 'Гилдмастеры'),
        ('quest', 'Квестгиверы'),
        ('smith', 'Кузнецы'),
        ('tanner', 'Кожевники'),
        ('potion', 'Зельевары'),
        ('spellmaster', 'Мастера заклинаний'),
    )
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    category = models.CharField(max_length=16, choices=TYPE, default='tank')
    text = RichTextField()
    creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} by {self.author}, {self.category}.'


class UserResponse(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.TextField()
    creation = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    class Meta:
        ordering = ['-creation']

    def __str__(self):
        return f'{self.author}. {self.creation}: {self.text}'


class OneTimeCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=10)
    creation = models.DateTimeField(auto_now_add=True)


class MassMail(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} - {self.creation}'