#-*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date


class pelicula(models.Model):
    _name = 'filmotecacarla.pelicula'
    _description = 'filmotecacarla.pelicula'
    
    code = fields.Char(string="Código", compute = "_get_code")
    name = fields.Char(string="Nombre", readonly = False, required = True, help = "Introduzca el nombre")
    description = fields.Text(string="Descripción")
    film_date = fields.Date(string="Fecha de estreno")
    start_date = fields.Date(string="Fecha de inicio")
    end_date = fields.Date(string="Fecha de fin")
    languaje = fields.Selection([('es', 'Español'), ('in', 'Inglés'), ('al', 'Alemán'), ('fr', 'Francés')], string="Idioma", default='es')
    opinion = fields.Selection([('0', 'Mala'), ('1', 'Regular'), ('2', 'Buena')], string="Opinión", default='1')
    color = fields.Selection([('color', 'Color'), ('bw', 'Blanco y negro')], string="Formato Color", default='color')
    is_spanish = fields.Boolean(string="¿Española?")
    image = fields.Image(string="Cartel", max_width=1024, max_height=1024)
    
    
    genero_id = fields.Many2one("filmotecacarla.genero", string = "Género", required = True, ondelete = "cascade")
    tecnicas_id = fields.Many2many(comodel_name = "filmotecacarla.tecnica", relation = "tecnicas_peliculas", 
                                   column1 = "tecnicas_ids", column2 = "peliculas_ids")
    
    #@api.one Para recibir un único objeto
    def _get_code(self):
        for pelicula in self:
            if len(pelicula.genero_id) == 0:
                pelicula.code = "FILM_" + str(pelicula.id)
            else:
                pelicula.code = str(pelicula.genero_id.name).upper() + "_" + str(pelicula.id)
                
    def toggle_spanish(self):
        self.is_spanish = not self.is_spanish
        
    def f_create(self):
        pelicula = {
            "name" : "Prueba ORM",
            "color" : "color",
            "genero_id": 1,
            "start_date" : str(date(2022, 8, 8))
        }
        print(pelicula)
        self.env['filmotecacarla.pelicula'].create(pelicula)
        
    #@api.one Para recibir un único objeto
    def f_search_update(self):
        pelicula = self.env['filmotecacarla.pelicula'].search([('name', '=', self.name)])
        print('search()', pelicula, pelicula.name)
            
        pelicula.write({
            "name": pelicula.name + " EDITADO"
        })
        
    def f_delete(self):
        pelicula = self.env['filmotecacarla.pelicula'].browse([self.id])
        pelicula.unlink()