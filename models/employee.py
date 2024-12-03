from odoo.odoo import fields, models


class EmployeeModel(models.Model):
    _name = "conge.employee"
    _inherit = "conge.user"

    matricule = fields.Char("Numéro matricule")
    poste_id = fields.Many2one("conge.user.poste", string='Poste')
