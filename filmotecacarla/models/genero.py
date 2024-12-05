#-*- coding: utf-8 -*-

from odoo import models, fields, api


class genero(models.Model):
    _name = 'filmotecacarla.genero'
    _description = 'filmotecacarla.genero'
     
    name = fields.Char(string="Nombre", readonly = False, required = True, help = "Introduzca el nombre")
    description = fields.Text(string="Descripción")
    
    peliculas_id = fields.One2many(string = "Películas", comodel_name = "filmotecacarla.pelicula", inverse_name = "genero_id")