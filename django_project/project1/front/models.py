# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DongguangWeather(models.Model):
    date1 = models.CharField(max_length=20, blank=True, null=True)
    weather_condition1 = models.CharField(db_column='Weather_condition1', max_length=10, blank=True,
                                          null=True)  # Field name made lowercase.
    weather_condition2 = models.CharField(db_column='Weather_condition2', max_length=10, blank=True,
                                          null=True)  # Field name made lowercase.
    high_temperature = models.CharField(max_length=10, blank=True, null=True)
    low_temperature = models.CharField(max_length=10, blank=True, null=True)
    wind_direction1 = models.CharField(db_column='Wind_direction1', max_length=20, blank=True,
                                       null=True)  # Field name made lowercase.
    wind_direction2 = models.CharField(db_column='Wind_direction2', max_length=20, blank=True,
                                       null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'dongguang_weather'


class FoshanWeather(models.Model):
    date1 = models.CharField(max_length=20, blank=True, null=True)
    weather_condition1 = models.CharField(db_column='Weather_condition1', max_length=10, blank=True,
                                          null=True)  # Field name made lowercase.
    weather_condition2 = models.CharField(db_column='Weather_condition2', max_length=10, blank=True,
                                          null=True)  # Field name made lowercase.
    high_temperature = models.CharField(max_length=10, blank=True, null=True)
    low_temperature = models.CharField(max_length=10, blank=True, null=True)
    wind_direction1 = models.CharField(db_column='Wind_direction1', max_length=20, blank=True,
                                       null=True)  # Field name made lowercase.
    wind_direction2 = models.CharField(db_column='Wind_direction2', max_length=20, blank=True,
                                       null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'foshan_weather'


class GuangzhouWeather(models.Model):
    date1 = models.CharField(max_length=20, blank=True, null=True)
    weather_condition1 = models.CharField(db_column='Weather_condition1', max_length=10, blank=True,
                                          null=True)  # Field name made lowercase.
    weather_condition2 = models.CharField(db_column='Weather_condition2', max_length=10, blank=True,
                                          null=True)  # Field name made lowercase.
    high_temperature = models.CharField(max_length=10, blank=True, null=True)
    low_temperature = models.CharField(max_length=10, blank=True, null=True)
    wind_direction1 = models.CharField(db_column='Wind_direction1', max_length=20, blank=True,
                                       null=True)  # Field name made lowercase.
    wind_direction2 = models.CharField(db_column='Wind_direction2', max_length=20, blank=True,
                                       null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'guangzhou_weather'


class HuizhouWeather(models.Model):
    date1 = models.CharField(max_length=20, blank=True, null=True)
    weather_condition1 = models.CharField(db_column='Weather_condition1', max_length=10, blank=True,
                                          null=True)  # Field name made lowercase.
    weather_condition2 = models.CharField(db_column='Weather_condition2', max_length=10, blank=True,
                                          null=True)  # Field name made lowercase.
    high_temperature = models.CharField(max_length=10, blank=True, null=True)
    low_temperature = models.CharField(max_length=10, blank=True, null=True)
    wind_direction1 = models.CharField(db_column='Wind_direction1', max_length=50, blank=True,
                                       null=True)  # Field name made lowercase.
    wind_direction2 = models.CharField(db_column='Wind_direction2', max_length=50, blank=True,
                                       null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'huizhou_weather'


class JiangmenWeather(models.Model):
    date1 = models.CharField(max_length=20, blank=True, null=True)
    weather_condition1 = models.CharField(db_column='Weather_condition1', max_length=10, blank=True,
                                          null=True)  # Field name made lowercase.
    weather_condition2 = models.CharField(db_column='Weather_condition2', max_length=10, blank=True,
                                          null=True)  # Field name made lowercase.
    high_temperature = models.CharField(max_length=10, blank=True, null=True)
    low_temperature = models.CharField(max_length=10, blank=True, null=True)
    wind_direction1 = models.CharField(db_column='Wind_direction1', max_length=50, blank=True,
                                       null=True)  # Field name made lowercase.
    wind_direction2 = models.CharField(db_column='Wind_direction2', max_length=50, blank=True,
                                       null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'jiangmen_weather'


class MaomingWeather(models.Model):
    date1 = models.CharField(max_length=20, blank=True, null=True)
    weather_condition1 = models.CharField(db_column='Weather_condition1', max_length=10, blank=True,
                                          null=True)  # Field name made lowercase.
    weather_condition2 = models.CharField(db_column='Weather_condition2', max_length=10, blank=True,
                                          null=True)  # Field name made lowercase.
    high_temperature = models.CharField(max_length=10, blank=True, null=True)
    low_temperature = models.CharField(max_length=10, blank=True, null=True)
    wind_direction1 = models.CharField(db_column='Wind_direction1', max_length=50, blank=True,
                                       null=True)  # Field name made lowercase.
    wind_direction2 = models.CharField(db_column='Wind_direction2', max_length=50, blank=True,
                                       null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'maoming_weather'


class ShantouWeather(models.Model):
    date1 = models.CharField(max_length=20, blank=True, null=True)
    weather_condition1 = models.CharField(db_column='Weather_condition1', max_length=10, blank=True,
                                          null=True)  # Field name made lowercase.
    weather_condition2 = models.CharField(db_column='Weather_condition2', max_length=10, blank=True,
                                          null=True)  # Field name made lowercase.
    high_temperature = models.CharField(max_length=10, blank=True, null=True)
    low_temperature = models.CharField(max_length=10, blank=True, null=True)
    wind_direction1 = models.CharField(db_column='Wind_direction1', max_length=20, blank=True,
                                       null=True)  # Field name made lowercase.
    wind_direction2 = models.CharField(db_column='Wind_direction2', max_length=20, blank=True,
                                       null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'shantou_weather'


class ShaoguanWeather(models.Model):
    date1 = models.CharField(max_length=20, blank=True, null=True)
    weather_condition1 = models.CharField(db_column='Weather_condition1', max_length=10, blank=True,
                                          null=True)  # Field name made lowercase.
    weather_condition2 = models.CharField(db_column='Weather_condition2', max_length=10, blank=True,
                                          null=True)  # Field name made lowercase.
    high_temperature = models.CharField(max_length=10, blank=True, null=True)
    low_temperature = models.CharField(max_length=10, blank=True, null=True)
    wind_direction1 = models.CharField(db_column='Wind_direction1', max_length=20, blank=True,
                                       null=True)  # Field name made lowercase.
    wind_direction2 = models.CharField(db_column='Wind_direction2', max_length=20, blank=True,
                                       null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'shaoguan_weather'


class ShenzhenWeather(models.Model):
    date1 = models.CharField(max_length=20, blank=True, null=True)
    weather_condition1 = models.CharField(db_column='Weather_condition1', max_length=10, blank=True,
                                          null=True)  # Field name made lowercase.
    weather_condition2 = models.CharField(db_column='Weather_condition2', max_length=10, blank=True,
                                          null=True)  # Field name made lowercase.
    high_temperature = models.CharField(max_length=10, blank=True, null=True)
    low_temperature = models.CharField(max_length=10, blank=True, null=True)
    wind_direction1 = models.CharField(db_column='Wind_direction1', max_length=20, blank=True,
                                       null=True)  # Field name made lowercase.
    wind_direction2 = models.CharField(db_column='Wind_direction2', max_length=20, blank=True,
                                       null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'shenzhen_weather'


class ZhanjiangWeather(models.Model):
    date1 = models.CharField(max_length=20, blank=True, null=True)
    weather_condition1 = models.CharField(db_column='Weather_condition1', max_length=10, blank=True,
                                          null=True)  # Field name made lowercase.
    weather_condition2 = models.CharField(db_column='Weather_condition2', max_length=10, blank=True,
                                          null=True)  # Field name made lowercase.
    high_temperature = models.CharField(max_length=10, blank=True, null=True)
    low_temperature = models.CharField(max_length=10, blank=True, null=True)
    wind_direction1 = models.CharField(db_column='Wind_direction1', max_length=50, blank=True,
                                       null=True)  # Field name made lowercase.
    wind_direction2 = models.CharField(db_column='Wind_direction2', max_length=50, blank=True,
                                       null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'zhanjiang_weather'


class ZhaoqingWeather(models.Model):
    date1 = models.CharField(max_length=20, blank=True, null=True)
    weather_condition1 = models.CharField(db_column='Weather_condition1', max_length=10, blank=True,
                                          null=True)  # Field name made lowercase.
    weather_condition2 = models.CharField(db_column='Weather_condition2', max_length=10, blank=True,
                                          null=True)  # Field name made lowercase.
    high_temperature = models.CharField(max_length=10, blank=True, null=True)
    low_temperature = models.CharField(max_length=10, blank=True, null=True)
    wind_direction1 = models.CharField(db_column='Wind_direction1', max_length=50, blank=True,
                                       null=True)  # Field name made lowercase.
    wind_direction2 = models.CharField(db_column='Wind_direction2', max_length=50, blank=True,
                                       null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'zhaoqing_weather'


class ZhongshanWeather(models.Model):
    date1 = models.CharField(max_length=20, blank=True, null=True)
    weather_condition1 = models.CharField(db_column='Weather_condition1', max_length=10, blank=True,
                                          null=True)  # Field name made lowercase.
    weather_condition2 = models.CharField(db_column='Weather_condition2', max_length=10, blank=True,
                                          null=True)  # Field name made lowercase.
    high_temperature = models.CharField(max_length=10, blank=True, null=True)
    low_temperature = models.CharField(max_length=10, blank=True, null=True)
    wind_direction1 = models.CharField(db_column='Wind_direction1', max_length=20, blank=True,
                                       null=True)  # Field name made lowercase.
    wind_direction2 = models.CharField(db_column='Wind_direction2', max_length=20, blank=True,
                                       null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'zhongshan_weather'


class ZhuhaiWeather(models.Model):
    date1 = models.CharField(max_length=20, blank=True, null=True)
    weather_condition1 = models.CharField(db_column='Weather_condition1', max_length=10, blank=True,
                                          null=True)  # Field name made lowercase.
    weather_condition2 = models.CharField(db_column='Weather_condition2', max_length=10, blank=True,
                                          null=True)  # Field name made lowercase.
    high_temperature = models.CharField(max_length=10, blank=True, null=True)
    low_temperature = models.CharField(max_length=10, blank=True, null=True)
    wind_direction1 = models.CharField(db_column='Wind_direction1', max_length=20, blank=True,
                                       null=True)  # Field name made lowercase.
    wind_direction2 = models.CharField(db_column='Wind_direction2', max_length=20, blank=True,
                                       null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'zhuhai_weather'


class TestData1(models.Model):
    high_temperature = models.BigIntegerField()
    low_temperature = models.BigIntegerField()
    weather_condition1 = models.BigIntegerField()
    weather_condition2 = models.BigIntegerField()  # Field name made lowercase.
    wind_direction1 = models.BigIntegerField()  # Field name made lowercase.
    wind_direction2 = models.BigIntegerField()  # Field name made lowercase.

    class Meta:
        db_table = 'test_data1'


class ImageData(models.Model):
    img_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'img_address'
