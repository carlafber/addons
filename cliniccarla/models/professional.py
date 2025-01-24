#-*- coding: utf-8 -*-

from odoo import models, fields, api

class professional(models.Model):
    _name = 'cliniccarla.professional'
    _description = 'cliniccarla.professional'
    
    name = fields.Char(string = "Nombre", required = True, help = "Introduzca el nombre del profesional")
    surnames = fields.Char(string = "Apellidos", required = True, help = "Introduzca los apellidos del profesional")
    type_of = fields.Selection([
        ('musc', 'Muscular'),
        ('dep', 'Deportivo'),
        ('ger', 'Geriátrico'),
        ('ped', 'Pediátrico')
    ], string="Tipo", help = "Seleccione el tipo de profesional")
    phone = fields.Char(string = "Teléfono", help = "Introduzca el teléfono del profesional")
    mail = fields.Char(string = "Correo", help = "Introduzca el correo del profesional")
    
    
    #Campo de la relación entre profesionales y tratamientos
    treatments_id = fields.One2many(string = "Tratamientos", comodel_name = "cliniccarla.treatment", inverse_name = "professional_id")
    
    #Campo computado que contiene todas las sesiones de un profesional
    asigned_sessions = fields.Many2many("cliniccarla.session", string = "Sesiones", compute = "_get_asigned_sessions")
    
    #Función que asigna las sesiones al profesional
    def _get_asigned_sessions(self):
        for professional in self: #recorro el profesional
            sessions = None #creo una lista vacía de sesiones
            for treatment in professional.treatments_id: #recorro cada tratamiento del profesional
                if not sessions: #si aun no he añadido ninguna sesión se pone la primera
                    sessions = treatment.sessions_id
                else: #las demás sesiones se añaden al final de la lista de todas las sesiones
                    sessions = sessions + treatment.sessions_id
            professional.asigned_sessions = sessions #asigno al campo la lista con todas las sesiones