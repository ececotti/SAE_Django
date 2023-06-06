from django import forms 
from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MaxValueValidator
from django.shortcuts import render
from .models import Machine, Personnel
import ipaddress


class AddMachineForm(forms.Form):
    RESEAU_MACHINE = (
        ('Filiale', 'Filiale - 192.168.0.0'),
        ('QG', 'QG - 10.10.10.0'),
        ('Serveurs', 'Serveurs - 172.22.16.0'),
        ('WifiOuvert', 'WifiOuvert - 122.0.0.0'),
        ('BackUp', 'BackUp - 156.123.0.0'),
    )

    TYPE_MACHINE = (
        ('PC', 'PC - Run Windows'),
        ('Mac', 'Mac - Run MacOS'),
        ('Serveur', 'Serveur - Simple Server to deploy virtual machines'),
        ('Switch', 'Switch - To maintain and connect servers'),
        ('Rooter', 'Rooter - To maintain and connect LANs'),
    )

    name = forms.CharField(required=True, label='Nom de la machine')
    reseau = forms.ChoiceField(choices=RESEAU_MACHINE, label='Nom du réseau')
    id = forms.CharField(required=True, label='Id de la machine')
    ip = forms.GenericIPAddressField(required=True, label='Adresse IP de la machine')
    machine_type = forms.ChoiceField(choices=TYPE_MACHINE, label='Type de la machine')

    def clean_name(self):
        data = self.cleaned_data["name"]
        if len(data) > 60:
            raise ValidationError("Erreur de format pour le champ nom")
        return data

    def clean_id(self):
        data = self.cleaned_data["id"]
        if len(data) > 60:
            raise ValidationError("Erreur de format pour le champ id")
        return data

    def clean_ip(self):
        data = self.cleaned_data["ip"]
        try:
            ipaddress.ip_address(data)
        except ValueError:
            raise forms.ValidationError("Veuillez entrer une adresse IP valide.")
        return data

    def clean_reseau(self):
        data = self.cleaned_data["reseau"]
        if len(data) > 60:
            raise forms.ValidationError("Erreur de format pour le champ reseau")
        return data
    
    def clean_type(self):
        data = self.cleaned_data["machine_type"]
        if len(data) > 32:
            raise ValidationError("Erreur de format pour le champ type")
        return data
    
        
class AddPersonnelForm (forms.Form):

    nom = forms.CharField (required=True, label = 'Nom de la personnel')
    prenom = forms.CharField (required=True, label = 'Prenom de la personnel')
    id = forms.IntegerField (required=True, label='ID svp de la personne')
    machine = machine = forms.ModelChoiceField(queryset=Machine.objects.all(), required=False)
    
    def clean_nom(self):
        data = self.cleaned_data["nom"]
        if len(data) > 60:
            raise ValidationError (("Erreur de format pour le champ nom"))
        return data

    def clean_id(self):
        data_p=self.cleaned_data["id"]
        if data_p < 1000000000000 and data_p > 2999999999999:
            raise ValidationError(("Erreur de format pour le champ id"))
        return data_p

    def clean_prenom(self):
        data = self.cleaned_data["prenom"]
        if len(data) > 60:
            raise ValidationError (("Erreur de format pour le champ prenom"))
        return data
    
class SearchForm (forms.Form):
    personnel_name = forms.CharField(label='Nom du personnel', required=False)
    machine_name = forms.CharField(label='Nom de la machine', required=False)
    machine_ip = forms.GenericIPAddressField(label='Adresse IP de la machine', required=False)

