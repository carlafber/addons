#-*- coding: utf-8 -*-

from odoo import models, fields, api

class tecnica(models.Model):
    _name = 'filmotecacarla.tecnica'
    _description = 'filmotecacarla.tecnica'
     
    name = fields.Char(string="Nombre")
    description = fields.Text(string="Descripción")
    
    photo = fields.Image(string="Imagen")
    
    peliculas_id = fields.Many2many(string = "Películas", 
                                    comodel_name = "filmotecacarla.pelicula", 
                                    relation = "tecnicas_peliculas", column1 = "peliculas_ids", column2 = "tecnicas_ids")