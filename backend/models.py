# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

#Se crea el modelo correspondiente a la tabla que almacena la información en MySQL
class Criptomonedas(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100)  # Field name made lowercase.
    simbolo = models.CharField(db_column='Símbolo', max_length=10)  # Field name made lowercase.
    precio_usd_field = models.CharField(db_column='Precio (USD)', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    vol_24h_field = models.CharField(db_column='Vol. (24h)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    vol_total = models.CharField(db_column='Vol. Total', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    var_24h_field = models.CharField(db_column='Var. (24h)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    var_7d_field = models.CharField(db_column='Var. (7d)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    cap_mercado = models.CharField(db_column='Cap. mercado', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'criptomonedas'
