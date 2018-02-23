from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        verbose_name='posts')
    title = models.CharField(
        max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Publication(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        verbose_name='author',
        related_name='publications')
    text_file = models.FileField(
        upload_to='publications')
    title = models.CharField(
        max_length=200)
    publication_date = models.DateTimeField(
        blank=True,
        null=True)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(
        'auth.User',
        on_delete=models.CASCADE,
        verbose_name='profile')
    title = models.CharField(
        max_length=200)
    hierarchy = models.IntegerField(
        default=1)
    avatar = models.ImageField(
        blank=True,
        upload_to='avatars')
    position = models.CharField(
        max_length=200,
        help_text='Position in terms of department')
    info = models.TextField(
        blank=True,
        help_text='Any additional information')
    text = models.TextField(
        blank=True,
        help_text='Any additional information')
    published_date = models.DateTimeField(
        blank=True,
        null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class PageWithTests(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        verbose_name='author',
        related_name='pageWithTests')
    text_file = models.FileField(
        upload_to='pageWithTests')
    title = models.CharField(
        max_length=200)
    text = models.TextField(
        blank=True,
        help_text='Any information')
    publication_date = models.DateTimeField(
        blank=True,
        null=True)

    def __str__(self):
        return self.title