# Generated by Django 3.1.4 on 2021-02-11 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='news',
            new_name='news_name',
        ),
    ]