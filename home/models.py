from django.db import models

# Create your models here.
class Proveedor(models.Model):
    id_prov = models.CharField(max_length=12, null=False, blank=False, primary_key=True)
    nom_proveedor = models.CharField(max_length=50, null=False, blank=False)


    def __str__(self):
        return self.id_prov + " - " + self.nom_proveedor

class Articulo(models.Model):
    cod_art = models.CharField(max_length=50, unique=True, null=False, blank=False, primary_key=True)
    descrip_art = models.CharField(max_length=100, null=True, blank=True)
    stock_bod= models.IntegerField( null=True, blank=True)
    id_prov = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.cod_art + "-" + self.descrip_art


class Ventas(models.Model):
    cod_art =  models.CharField(max_length=100, null=True, blank=True)
    cant_vent= models.IntegerField(null=True, blank=True)


class StockMinimoProductos(models.Model):
    cod_art =  models.CharField(max_length=100, null=True, blank=True)
    min_mat= models.IntegerField(null=True, blank=True)
    min_bul= models.IntegerField(null=True, blank=True)
    min_bod= models.IntegerField(null=True, blank=True)

class StockMinimo(models.Model):
    cod_art =  models.CharField(max_length=100, null=True, blank=True)
    min_mat= models.IntegerField(null=True, blank=True)
    min_bul= models.IntegerField(null=True, blank=True)
    min_bod= models.IntegerField(null=True, blank=True)
