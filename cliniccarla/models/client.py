#-*- coding: utf-8 -*-

from odoo import models, fields, api

class client(models.Model):
    _name = 'cliniccarla.client'
    _description = 'cliniccarla.client'
    
    name = fields.Char(string = "Nombre", required = True, help = "Introduzca el nombre del cliente")
    surnames = fields.Char(string = "Apellidos", required = True, help = "Introduzca los apellidos del cliente")
    birth_date = fields.Datetime(string="Fecha de nacimiento", help = "Introduzca la fecha de nacimiento del cliente")
    phone = fields.Char(string = "Teléfono", help = "Introduzca el teléfono del cliente")
    mail = fields.Char(string = "Correo", help = "Introduzca el correo del cliente")
    address = fields.Char(string = "Dirección", help = "Introduzca la dirección del cliente")
    
    #Campo de la relación entre clientes y registros
    registers_id = fields.One2many(string = "Registros", comodel_name = "cliniccarla.register", inverse_name = "client_id")