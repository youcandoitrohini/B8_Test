# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class City(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=35)  # Field name made lowercase.
    countrycode = models.ForeignKey('Country', models.DO_NOTHING, db_column='CountryCode')  # Field name made lowercase.
    district = models.CharField(db_column='District', max_length=20)  # Field name made lowercase.
    population = models.IntegerField(db_column='Population')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'city'


class Country(models.Model):
    code = models.CharField(db_column='Code', primary_key=True, max_length=3)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=52)  # Field name made lowercase.
    continent = models.CharField(db_column='Continent', max_length=13)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=26)  # Field name made lowercase.
    surfacearea = models.DecimalField(db_column='SurfaceArea', max_digits=10, decimal_places=2)  # Field name made lowercase.
    indepyear = models.SmallIntegerField(db_column='IndepYear', blank=True, null=True)  # Field name made lowercase.
    population = models.IntegerField(db_column='Population')  # Field name made lowercase.
    lifeexpectancy = models.DecimalField(db_column='LifeExpectancy', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    gnp = models.DecimalField(db_column='GNP', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    gnpold = models.DecimalField(db_column='GNPOld', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localname = models.CharField(db_column='LocalName', max_length=45)  # Field name made lowercase.
    governmentform = models.CharField(db_column='GovernmentForm', max_length=45)  # Field name made lowercase.
    headofstate = models.CharField(db_column='HeadOfState', max_length=60, blank=True, null=True)  # Field name made lowercase.
    capital = models.IntegerField(db_column='Capital', blank=True, null=True)  # Field name made lowercase.
    code2 = models.CharField(db_column='Code2', max_length=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'country'


class Countrylanguage(models.Model):
    countrycode = models.OneToOneField(Country, models.DO_NOTHING, db_column='CountryCode', primary_key=True)  # Field name made lowercase.
    language = models.CharField(db_column='Language', max_length=30)  # Field name made lowercase.
    isofficial = models.CharField(db_column='IsOfficial', max_length=1)  # Field name made lowercase.
    percentage = models.DecimalField(db_column='Percentage', max_digits=4, decimal_places=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'countrylanguage'
        unique_together = (('countrycode', 'language'),)
