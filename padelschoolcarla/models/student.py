#-*- coding: utf-8 -*-

from odoo import models, fields, api

class student(models.Model):
    _name = 'padelschoolcarla.student'
    _description = 'padelschoolcarla.student'
    
    name = fields.Char(string = "Nombre", required = True, help = "Introduzca el nombre del alumno")
    surnames = fields.Char(string = "Apellidos", required = True, help = "Introduzca los apellidos del alumno")
    mail = fields.Char(string = "Correo", help = "Introduzca el correo del alumno")
    phone = fields.Integer(string = "Teléfono", help = "Introduzca el teléfono del alumno")
    
    
    courses_id = fields.Many2many(string = "Cursos", comodel_name = "padelschoolcarla.course", relation = "alumnos_cursos", 
                                   column1 = "cursos_ids", column2 = "estudiantes_ids")