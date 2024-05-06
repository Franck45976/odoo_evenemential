from odoo import models, fields, api

  #Création, modification et suppression d'événements avec titre, description, date, lieu, etc.
class GestionEvenemnt(models.Model):

    _name = 'gestion_evenemnt'
    _description = 'gestion des événements'

    name = fields.Char(string='Titre')
    description = fields.Char(string='Description')
    date_debut = fields.Date(string='Date Debut')
    date_fin = fields.Date(string='Date Fin')
    lieu = fields.Char(string='Lieu')



class InscriptionLigne(models.Model):

    _name = 'inscription_ligne'
    _description = ''

    







