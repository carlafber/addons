#-*- coding: utf-8 -*-

from odoo import models, fields, api

class session(models.Model):
    _name = 'cliniccarla.session'
    _description = 'cliniccarla.session'
    
    name = fields.Char(string = "Nombre", required = True, help = "Introduzca el nombre de la sesión")
    description = fields.Text(string = "Descripción", help = "Introduzca una descripción de la sesión")
    date = fields.Datetime(string="Fecha", help = "Introduzca la fecha de la sesión")
    
    #Campo de la relación entre sesiones y tratamientos
    treatment_id = fields.Many2one("cliniccarla.treatment", string = "Tratamiento", required = True, ondelete = "cascade")
    #Campo de la relación entre sesiones y técnicas
    techniques_id = fields.Many2many(string = "Técnicas", comodel_name = "cliniccarla.technique", relation = "sesiones_tecnicas", 
                                   column1 = "tecnicas_ids", column2 = "sesiones_ids")
    #Campo que muestra el nombre del profesional
    professional_session = fields.Many2many("cliniccarla.professional", string = "Profesional", readonly = True, compute = "_get_professional_session")
    
    #Función que asigna el nombre del profesional a la sesión
    @api.depends('treatment_id.professional_id') #depende de esa relación
    def _get_professional_session(self):
        for session in self: #recorro la sesión
            all_professionals = session.treatment_id.mapped('professional_id') #creo una lista de profesionales que asigna los profesionales del tratamiento
            session.professional_session = all_professionals #asigno los valores de la lista al campo