# -*- coding: utf-8 -*-
# from odoo import http


# class Cliniccarla(http.Controller):
#     @http.route('/cliniccarla/cliniccarla', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cliniccarla/cliniccarla/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('cliniccarla.listing', {
#             'root': '/cliniccarla/cliniccarla',
#             'objects': http.request.env['cliniccarla.cliniccarla'].search([]),
#         })

#     @http.route('/cliniccarla/cliniccarla/objects/<model("cliniccarla.cliniccarla"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cliniccarla.object', {
#             'object': obj
#         })
