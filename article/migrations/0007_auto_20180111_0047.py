# Generated by Django 2.0.1 on 2018-01-10 18:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20180111_0046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='date',
        ),
        migrations.AddField(
            model_name='comments',
            name='comments_date',
            field=models.DateTimeField(auto_now=True, verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 1, 10, 18, 47, 35, 27016, tzinfo=utc)),
        ),
    ]
