# Generated by Django 2.0 on 2019-07-24 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('massage', '0016_auto_20190724_1635'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['age', 'create_time']},
        ),
    ]
