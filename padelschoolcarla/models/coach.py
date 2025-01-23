#-*- coding: utf-8 -*-

from odoo import models, fields, api

class coach(models.Model):
    _name = 'padelschoolcarla.coach'
    _description = 'padelschoolcarla.coach'
    
    name = fields.Char(string = "Nombre", required = True, help = "Introduzca el nombre del monitor")
    surnames = fields.Char(string = "Apellidos", required = True, help = "Introduzca los apellidos del monitor")
    mail = fields.Char(string = "Correo", help = "Introduzca el correo del monitor")
    phone = fields.Integer(string = "Teléfono", help = "Introduzca el teléfono del monitor")
    
    
    courses_id = fields.One2many(string = "Cursos", comodel_name = "padelschoolcarla.course", inverse_name = "coach_id")