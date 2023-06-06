from django.db import models
from django.core.validators import MaxValueValidator
from datetime import datetime


class Machine(models.Model):
    id = models.AutoField(
        #permet de faire qu'il y a cette info
        primary_key=True,
        editable=False)
    
    def __str__(self):
        return str(self.id) + " --> " + self.name + ", " + self.reseau
    
    def get_name(self):
        return str(self.id) + " " + self.name + ", " + self.reseau
    
    TYPE = (
        ('PC', ('PC - Run windows')),
        ('Mac', ('MAc - Run MacOS')),
        ('Serveur', ('Serveur - Simple Server to deploy virtual machines')),
        ('Switch', ('Switch − To maintains and connect servers' )),
        ('Rooter', ('Rooter - To maintains and connect LANs')),
    )
    
    reseau = (
        ('Filiale', ('Filiale - 192.168.0.0')),
        ('QG', ('QG - 10.10.10.0')),
        ('Serveurs', ('Serveurs - 172.22.16.0')),
        ('WifiOuvert', ('WifiOuvert − 122.0.0.0' )),
        ('BackUp', ('BackUp - 156.123.0.0')),
    )
    
    type_machine = models.CharField(max_length=200, default ='')
    reseau = models.CharField(max_length=200, default ='')
    name = models.CharField(max_length=6, default ='')
    ip = models.GenericIPAddressField(null=True)
    maintenanceDate = models.DateField(default = datetime.now())
    
class Personnel(models.Model):
    
    id = models.PositiveIntegerField(primary_key=True,editable=True, validators=[MaxValueValidator(9999999999999)])
    nom= models.CharField(max_length= 200)
    prenom= models.CharField(max_length= 200)
    machine = models.ForeignKey(Machine, on_delete=models.SET_NULL, null=True)
        
    #donne ce qui est affiché sur le site
    def __str__(self):
        return str(self.id) + " --> " + self.nom + ", " + self.prenom + ", " + self.machine
 

