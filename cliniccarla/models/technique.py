#-*- coding: utf-8 -*-

from odoo import models, fields, api

class technique(models.Model):
    _name = 'cliniccarla.technique'
    _description = 'cliniccarla.technique'
    
    name = fields.Char(string = "Nombre", required = True, help = "Introduzca el nombre de la técinca")
    description = fields.Text(string = "Descripción", help = "Introduzca una descripción de la técinca")
    
    #Campo de la relación entre técnicas y sesiones
    sessions_id = fields.Many2many(string = "Sesiones", comodel_name = "cliniccarla.session", relation = "sesiones_tecnicas", 
                                   column1 = "sesiones_ids", column2 = "tecnicas_ids")