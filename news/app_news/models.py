from django.db import models


class News(models.Model):
    news_name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    date_create = models.DateField(auto_now_add=True)
    date_correct = models.DateTimeField(auto_now=True)
    activity = models.ForeignKey('Activity', on_delete=models.CASCADE, related_name="+", verbose_name='активность')

    class Meta:
        db_table = 'news'
        ordering = ['date_create']

    def __str__(self):
        return self.news_name


class Activity(models.Model):
    name = models.CharField(max_length=15)

    class Meta:
        db_table = "activity"
        ordering = ['name']

    def __str__(self):
        return self.name


class Comment(models.Model):
    news_name = models.ForeignKey('News', on_delete=models.CASCADE, related_name="comments", verbose_name='новость')
    user_name = models.CharField(max_length=15)
    text = models.CharField(max_length=300)
