# Generated by Django 2.0 on 2019-07-24 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('massage', '0017_auto_20190724_1640'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['age', 'username']},
        ),
    ]
