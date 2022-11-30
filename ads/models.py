from django.db import models

from users.models import User


class Ad(models.Model):
    title = models.CharField(max_length=150, null=False)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=1000, blank=True, null=True)
    author = models.ForeignKey(User, verbose_name='Автор', related_name='ads',
                               on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='ads', null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, verbose_name='Автор', related_name='comments',
                               on_delete=models.CASCADE, null=True)
    ad = models.ForeignKey(Ad, related_name='comments', verbose_name='Объявление', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
