
# Generated by Django 2.0 on 2019-08-21 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DongguangWeather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date1', models.CharField(blank=True, max_length=20, null=True)),
                ('weather_condition1', models.CharField(blank=True, db_column='Weather_condition1', max_length=10, null=True)),
                ('weather_condition2', models.CharField(blank=True, db_column='Weather_condition2', max_length=10, null=True)),
                ('high_temperature', models.CharField(blank=True, max_length=10, null=True)),
                ('low_temperature', models.CharField(blank=True, max_length=10, null=True)),
                ('wind_direction1', models.CharField(blank=True, db_column='Wind_direction1', max_length=20, null=True)),
                ('wind_direction2', models.CharField(blank=True, db_column='Wind_direction2', max_length=20, null=True)),
            ],
            options={
                'db_table': 'dongguang_weather',
            },
        ),
        migrations.CreateModel(
            name='FoshanWeather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date1', models.CharField(blank=True, max_length=20, null=True)),
                ('weather_condition1', models.CharField(blank=True, db_column='Weather_condition1', max_length=10, null=True)),
                ('weather_condition2', models.CharField(blank=True, db_column='Weather_condition2', max_length=10, null=True)),
                ('high_temperature', models.CharField(blank=True, max_length=10, null=True)),
                ('low_temperature', models.CharField(blank=True, max_length=10, null=True)),
                ('wind_direction1', models.CharField(blank=True, db_column='Wind_direction1', max_length=20, null=True)),
                ('wind_direction2', models.CharField(blank=True, db_column='Wind_direction2', max_length=20, null=True)),
            ],
            options={
                'db_table': 'foshan_weather',
            },
        ),
        migrations.CreateModel(
            name='GuangzhouWeather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date1', models.CharField(blank=True, max_length=20, null=True)),
                ('weather_condition1', models.CharField(blank=True, db_column='Weather_condition1', max_length=10, null=True)),
                ('weather_condition2', models.CharField(blank=True, db_column='Weather_condition2', max_length=10, null=True)),
                ('high_temperature', models.CharField(blank=True, max_length=10, null=True)),
                ('low_temperature', models.CharField(blank=True, max_length=10, null=True)),
                ('wind_direction1', models.CharField(blank=True, db_column='Wind_direction1', max_length=20, null=True)),
                ('wind_direction2', models.CharField(blank=True, db_column='Wind_direction2', max_length=20, null=True)),
            ],
            options={
                'db_table': 'guangzhou_weather',
            },
        ),
        migrations.CreateModel(
            name='HuizhouWeather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date1', models.CharField(blank=True, max_length=20, null=True)),
                ('weather_condition1', models.CharField(blank=True, db_column='Weather_condition1', max_length=10, null=True)),
                ('weather_condition2', models.CharField(blank=True, db_column='Weather_condition2', max_length=10, null=True)),
                ('high_temperature', models.CharField(blank=True, max_length=10, null=True)),
                ('low_temperature', models.CharField(blank=True, max_length=10, null=True)),
                ('wind_direction1', models.CharField(blank=True, db_column='Wind_direction1', max_length=50, null=True)),
                ('wind_direction2', models.CharField(blank=True, db_column='Wind_direction2', max_length=50, null=True)),
            ],
            options={
                'db_table': 'huizhou_weather',
            },
        ),
        migrations.CreateModel(
            name='JiangmenWeather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date1', models.CharField(blank=True, max_length=20, null=True)),
                ('weather_condition1', models.CharField(blank=True, db_column='Weather_condition1', max_length=10, null=True)),
                ('weather_condition2', models.CharField(blank=True, db_column='Weather_condition2', max_length=10, null=True)),
                ('high_temperature', models.CharField(blank=True, max_length=10, null=True)),
                ('low_temperature', models.CharField(blank=True, max_length=10, null=True)),
                ('wind_direction1', models.CharField(blank=True, db_column='Wind_direction1', max_length=50, null=True)),
                ('wind_direction2', models.CharField(blank=True, db_column='Wind_direction2', max_length=50, null=True)),
            ],
            options={
                'db_table': 'jiangmen_weather',
            },
        ),
        migrations.CreateModel(
            name='MaomingWeather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date1', models.CharField(blank=True, max_length=20, null=True)),
                ('weather_condition1', models.CharField(blank=True, db_column='Weather_condition1', max_length=10, null=True)),
                ('weather_condition2', models.CharField(blank=True, db_column='Weather_condition2', max_length=10, null=True)),
                ('high_temperature', models.CharField(blank=True, max_length=10, null=True)),
                ('low_temperature', models.CharField(blank=True, max_length=10, null=True)),
                ('wind_direction1', models.CharField(blank=True, db_column='Wind_direction1', max_length=50, null=True)),
                ('wind_direction2', models.CharField(blank=True, db_column='Wind_direction2', max_length=50, null=True)),
            ],
            options={
                'db_table': 'maoming_weather',
            },
        ),
        migrations.CreateModel(
            name='ShantouWeather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date1', models.CharField(blank=True, max_length=20, null=True)),
                ('weather_condition1', models.CharField(blank=True, db_column='Weather_condition1', max_length=10, null=True)),
                ('weather_condition2', models.CharField(blank=True, db_column='Weather_condition2', max_length=10, null=True)),
                ('high_temperature', models.CharField(blank=True, max_length=10, null=True)),
                ('low_temperature', models.CharField(blank=True, max_length=10, null=True)),
                ('wind_direction1', models.CharField(blank=True, db_column='Wind_direction1', max_length=20, null=True)),
                ('wind_direction2', models.CharField(blank=True, db_column='Wind_direction2', max_length=20, null=True)),
            ],
            options={
                'db_table': 'shantou_weather',
            },
        ),
        migrations.CreateModel(
            name='ShaoguanWeather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date1', models.CharField(blank=True, max_length=20, null=True)),
                ('weather_condition1', models.CharField(blank=True, db_column='Weather_condition1', max_length=10, null=True)),
                ('weather_condition2', models.CharField(blank=True, db_column='Weather_condition2', max_length=10, null=True)),
                ('high_temperature', models.CharField(blank=True, max_length=10, null=True)),
                ('low_temperature', models.CharField(blank=True, max_length=10, null=True)),
                ('wind_direction1', models.CharField(blank=True, db_column='Wind_direction1', max_length=20, null=True)),
                ('wind_direction2', models.CharField(blank=True, db_column='Wind_direction2', max_length=20, null=True)),
            ],
            options={
                'db_table': 'shaoguan_weather',
            },
        ),
        migrations.CreateModel(
            name='ShenzhenWeather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date1', models.CharField(blank=True, max_length=20, null=True)),
                ('weather_condition1', models.CharField(blank=True, db_column='Weather_condition1', max_length=10, null=True)),
                ('weather_condition2', models.CharField(blank=True, db_column='Weather_condition2', max_length=10, null=True)),
                ('high_temperature', models.CharField(blank=True, max_length=10, null=True)),
                ('low_temperature', models.CharField(blank=True, max_length=10, null=True)),
                ('wind_direction1', models.CharField(blank=True, db_column='Wind_direction1', max_length=20, null=True)),
                ('wind_direction2', models.CharField(blank=True, db_column='Wind_direction2', max_length=20, null=True)),
            ],
            options={
                'db_table': 'shenzhen_weather',
            },
        ),
        migrations.CreateModel(
            name='ZhanjiangWeather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date1', models.CharField(blank=True, max_length=20, null=True)),
                ('weather_condition1', models.CharField(blank=True, db_column='Weather_condition1', max_length=10, null=True)),
                ('weather_condition2', models.CharField(blank=True, db_column='Weather_condition2', max_length=10, null=True)),
                ('high_temperature', models.CharField(blank=True, max_length=10, null=True)),
                ('low_temperature', models.CharField(blank=True, max_length=10, null=True)),
                ('wind_direction1', models.CharField(blank=True, db_column='Wind_direction1', max_length=50, null=True)),
                ('wind_direction2', models.CharField(blank=True, db_column='Wind_direction2', max_length=50, null=True)),
            ],
            options={
                'db_table': 'zhanjiang_weather',
            },
        ),
        migrations.CreateModel(
            name='ZhaoqingWeather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date1', models.CharField(blank=True, max_length=20, null=True)),
                ('weather_condition1', models.CharField(blank=True, db_column='Weather_condition1', max_length=10, null=True)),
                ('weather_condition2', models.CharField(blank=True, db_column='Weather_condition2', max_length=10, null=True)),
                ('high_temperature', models.CharField(blank=True, max_length=10, null=True)),
                ('low_temperature', models.CharField(blank=True, max_length=10, null=True)),
                ('wind_direction1', models.CharField(blank=True, db_column='Wind_direction1', max_length=50, null=True)),
                ('wind_direction2', models.CharField(blank=True, db_column='Wind_direction2', max_length=50, null=True)),
            ],
            options={
                'db_table': 'zhaoqing_weather',
            },
        ),
        migrations.CreateModel(
            name='ZhongshanWeather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date1', models.CharField(blank=True, max_length=20, null=True)),
                ('weather_condition1', models.CharField(blank=True, db_column='Weather_condition1', max_length=10, null=True)),
                ('weather_condition2', models.CharField(blank=True, db_column='Weather_condition2', max_length=10, null=True)),
                ('high_temperature', models.CharField(blank=True, max_length=10, null=True)),
                ('low_temperature', models.CharField(blank=True, max_length=10, null=True)),
                ('wind_direction1', models.CharField(blank=True, db_column='Wind_direction1', max_length=20, null=True)),
                ('wind_direction2', models.CharField(blank=True, db_column='Wind_direction2', max_length=20, null=True)),
            ],
            options={
                'db_table': 'zhongshan_weather',
            },
        ),
        migrations.CreateModel(
            name='ZhuhaiWeather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date1', models.CharField(blank=True, max_length=20, null=True)),
                ('weather_condition1', models.CharField(blank=True, db_column='Weather_condition1', max_length=10, null=True)),
                ('weather_condition2', models.CharField(blank=True, db_column='Weather_condition2', max_length=10, null=True)),
                ('high_temperature', models.CharField(blank=True, max_length=10, null=True)),
                ('low_temperature', models.CharField(blank=True, max_length=10, null=True)),
                ('wind_direction1', models.CharField(blank=True, db_column='Wind_direction1', max_length=20, null=True)),
                ('wind_direction2', models.CharField(blank=True, db_column='Wind_direction2', max_length=20, null=True)),
            ],
            options={
                'db_table': 'zhuhai_weather',
            },
        ),
    ]
