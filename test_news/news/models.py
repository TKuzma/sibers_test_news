from django.db import models
from django.utils import timezone

class Article(models.Model):
    article_title = models.CharField('Article title', max_length=70)
    article_text = models.TextField('Article text')
    article_pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.article_title

