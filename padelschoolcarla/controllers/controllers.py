# -*- coding: utf-8 -*-
# from odoo import http


# class Padelschoolcarla(http.Controller):
#     @http.route('/padelschoolcarla/padelschoolcarla', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/padelschoolcarla/padelschoolcarla/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('padelschoolcarla.listing', {
#             'root': '/padelschoolcarla/padelschoolcarla',
#             'objects': http.request.env['padelschoolcarla.padelschoolcarla'].search([]),
#         })

#     @http.route('/padelschoolcarla/padelschoolcarla/objects/<model("padelschoolcarla.padelschoolcarla"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('padelschoolcarla.object', {
#             'object': obj
#         })
