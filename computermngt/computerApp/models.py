from django.db import models
from django.core.validators import MaxValueValidator
from datetime import datetime


class Machine(models.Model):
    id = models.AutoField(
        #permet de faire qu'il y a cette info
        primary_key=True,
        editable=False)
    
    def __str__(self):
        return str(self.id) + " --> " + self.name
    
    def get_name(self):
        return str(self.id) + " " + self.name
    
    TYPE = (
        ('PC', ('PC - Run windows')),
        ('Mac', ('MAc - Run MacOS')),
        ('Serveur', ('Serveur - Simple Server to deploy virtual machines')),
        ('Switch', ('Switch − To maintains and connect servers' )),
    )
    name = models.CharField(max_length=6, default ='')
    maintenanceDate = models.DateField(default = datetime.now())
    mach = models.CharField(max_length=32, choices=TYPE, default='PC')
    
class Personnel(models.Model):
    
    id = models.PositiveIntegerField(primary_key=True,editable=True, validators=[MaxValueValidator(9999999999999)])
    nom= models.CharField(max_length= 200)
    prenom= models.CharField(max_length= 200)
    
    #donne ce qui est affiché sur le site
    def __str__(self):
        return str(self.id) + " --> " + self.nom + ", " + self.prenom
 

