# Generated by Django 2.0 on 2019-07-24 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('massage', '0009_article_create_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='signature',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]