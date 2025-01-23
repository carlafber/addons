#-*- coding: utf-8 -*-

from odoo import models, fields, api

class course(models.Model):
    _name = 'padelschoolcarla.course'
    _description = 'padelschoolcarla.course'
    
    name = fields.Char(string = "Nombre", required = True, help = "Introduzca el nombre del curso")
    start_date = fields.Datetime(string = "Fecha de inicio", help = "Introduzca la fecha de inicio del curso")
    end_date = fields.Datetime(string = "Fecha de fin", help = "Introduzca la fecha de fin del curso")
    duration = fields.Integer(string = "Duración", help = "Introduzca la duración del curso")
    price = fields.Float(string = "Precio", help = "Introduzca el precio del curso")
    description = fields.Text(string = "Descripción", help = "Introduzca una breve descripción del curso")
    
    
    school_id = fields.Many2one("padelschoolcarla.school", string = "Escuela", required = True, ondelete = "cascade")
    coach_id = fields.Many2one("padelschoolcarla.coach", string = "Monitor", required = True, ondelete = "cascade")
    students_id = fields.Many2many(string = "Alumnos", comodel_name = "padelschoolcarla.student", relation = "alumnos_cursos", 
                                   column1 = "estudiantes_ids", column2 = "cursos_ids")