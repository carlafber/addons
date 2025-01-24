#-*- coding: utf-8 -*-

from odoo import models, fields, api

class register(models.Model):
    _name = 'cliniccarla.register'
    _description = 'cliniccarla.register'
    
    name = fields.Char(string = "Nombre", required = True, help = "Introduzca el nombre del registro")
    description = fields.Text(string = "Descripción", help = "Introduzca una descripción del registro")
    
    #Campo de la relación entre registros y clientes
    client_id = fields.Many2one("cliniccarla.client", string = "Cliente", required = True, ondelete = "cascade")
    #Campo de la relación entre registros y tratamientos
    treatments_id = fields.One2many(string = "Tratamientos", comodel_name = "cliniccarla.treatment", inverse_name = "register_id")