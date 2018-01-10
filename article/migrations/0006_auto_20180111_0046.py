# Generated by Django 2.0.1 on 2018-01-10 18:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20180111_0043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='comments_date',
        ),
        migrations.AddField(
            model_name='comments',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name=datetime.datetime(2018, 1, 10, 18, 46, 16, 527654, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 1, 10, 18, 46, 16, 527654, tzinfo=utc)),
        ),
    ]
