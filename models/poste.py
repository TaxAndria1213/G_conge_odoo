from odoo.odoo import fields, models


class PosteModel(models.Model):
    _name = "conge.user.poste"
    _description = "modèle de poste d'un employé dans la gestion de congé."

    name = fields.Char("Nom du poste")
    description = fields.Char("Description")
    employee_ids = fields.One2many("conge.employee", "poste_id", string="Employés associés")
