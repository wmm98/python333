# Generated by Django 2.0 on 2019-07-12 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('origin_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Comment')),
            ],
        ),
    ]
