#-*- coding: utf-8 -*-

from odoo import models, fields, api

class treatment(models.Model):
    _name = 'cliniccarla.treatment'
    _description = 'cliniccarla.treatment'
    
    name = fields.Char(string = "Nombre", required = True, readonly = True, help = "Introduzca el nombre del tratamiento", compute = "_get_name")
    description = fields.Text(string = "Descripción", help = "Introduzca una descripción del tratamiento")
    start_date = fields.Datetime(string="Fecha de inicio", help = "Introduzca la fecha de inicio del tratamiento")
    end_date = fields.Datetime(string="Fecha de fin", help = "Introduzca la fecha de fin del tratamiento")
    
    #Campo de la relación entre tratamientos y registros
    register_id = fields.Many2one("cliniccarla.register", string = "Registro", required = True, ondelete = "cascade")
    #Campo de la relación entre tratamientos y sesiones
    sessions_id = fields.One2many(string = "Sesiones", comodel_name = "cliniccarla.session", inverse_name = "treatment_id")
    #Campo de la relación entre tratamientos y profesionales
    professional_id = fields.Many2one("cliniccarla.professional", string = "Profesional", required = True, ondelete = "cascade")
    
    def _get_name(self):
        for treatment in self: #recorro el tratamiento
            for register in treatment.register_id: #recorro el registro del tratamiento
                #doy el nombre al tratamiento juntando el nombre del cliente del registro 
                #de ese tratamiento junto con el nombre del registro
                treatment.name = str(register.client_id.name) + " - " + str(register.name) 