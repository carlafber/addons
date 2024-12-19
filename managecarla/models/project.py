#-*- coding: utf-8 -*-

from odoo import models, fields, api

class project(models.Model):
    _name = 'managecarla.project'
    _description = 'managecarla.project'
    
    name = fields.Char(string="Nombre", readonly = False, required = True, help = "Introduzca el nombre")
    description = fields.Text(string="Descripción")
    
    
    histories_id = fields.One2many(string = "Historias", comodel_name = "managecarla.history", inverse_name = "project_id")
    
    sprints_id = fields.One2many(string = "Carreras", comodel_name = "managecarla.sprint", inverse_name = "project_id")    