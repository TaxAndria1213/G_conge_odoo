from odoo.odoo import models, fields


class UserModel(models.Model):
    _name = "conge.user"
    _description = "un modèle de l'utilisateur du gestion de congé"

    lastname = fields.Char("Nom")
    firstname = fields.Char("Prénom", required=True)
    mail = fields.Char("Email", required=True)
