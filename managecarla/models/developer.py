#-*- coding: utf-8 -*-

from odoo import models, fields, api

class developer(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    
    is_dev = fields.Boolean(string="¿Es Desarrollador?")
    
    technologies_id = fields.Many2many(string = "Tecnologías", comodel_name = "managecarla.technology", 
                                       relation = "developer_technologies",
                                       column1 = "developer_id", column2 = "technologies")
    
    @api.model
    def create(self, vals):
        # Si se crea un registro desde este modelo, el campo is_dev se marca como True
        vals['is_dev'] = True
        return super(developer, self).create(vals)