from django import forms 
from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MaxValueValidator

class AddMachineForm (forms.Form):

    nom = forms.CharField ( required = True , label = 'Nom de la machine')

    def clean_nom(self):
        data = self.cleaned_data["nom"]
        if len(data) > 60:
            raise ValidationError (("Erreur de format pour le champ nom"))
        return data
    
class AddPersonnelForm (forms.Form):

    nom = forms.CharField (required=True, label = 'Nom de la personnel')
    prenom = forms.CharField (required=True, label = 'Prenom de la personnel')
    id = forms.IntegerField (required=True, label='ID svp de la personne')
    
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