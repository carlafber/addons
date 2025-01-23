#-*- coding: utf-8 -*-

from odoo import models, fields, api

class school(models.Model):
    _name = 'padelschoolcarla.school'
    _description = 'padelschoolcarla.school'
    
    name = fields.Char(string = "Nombre", required = True, help = "Introduzca el nombre de la escuela")
    logo = fields.Image(string = "Imagen")
    address = fields.Char(string = "Dirección", help = "Introduzca la dirección de la escuela")
    mail = fields.Char(string = "Correo", help = "Introduzca el correo de la escuela")
    phone = fields.Integer(string = "Teléfono", help = "Introduzca el teléfono de la escuela")
    description = fields.Text(string = "Descripción", help = "Introduzca una descripción de la escuela")
    
    
    courses_id = fields.One2many(string = "Cursos", comodel_name = "padelschoolcarla.course", inverse_name = "school_id")
    
    students_school = fields.Many2many("padelschoolcarla.student", string = "Alumnos de la escuela", compute = "_get_students_school")
    
    def _get_students_school(self):
        for school in self:
            students = None
            for course in school.courses_id:
                if not students:
                    students = course.students_id
                else:
                    students = students + course.students_id
            school.students_school = students
            
    '''
    @api.depends('courses_id.students_id')
    def _get_students_school(self):
        for school in self:
            all_students = school.courses_id.mapped('students_id')
            school.students_school = all_students
    '''