# -*- coding: utf-8 -*-
# from odoo import http


# class Filmotecacarla(http.Controller):
#     @http.route('/filmotecacarla/filmotecacarla', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/filmotecacarla/filmotecacarla/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('filmotecacarla.listing', {
#             'root': '/filmotecacarla/filmotecacarla',
#             'objects': http.request.env['filmotecacarla.filmotecacarla'].search([]),
#         })

#     @http.route('/filmotecacarla/filmotecacarla/objects/<model("filmotecacarla.filmotecacarla"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('filmotecacarla.object', {
#             'object': obj
#         })

from odoo import http
from odoo.http import Response
import json


class pelicula_controller(http.Controller):

    @http.route('/api/peliculas', auth='public', method=['GET'], csrf=False)
    def get_peliculas(self, **kw):
        try:
            peliculas = http.request.env['filmotecacarla.pelicula'].sudo().search_read([], ['id', 'name', 'color'])
            res = json.dumps(peliculas, ensure_ascii=False).encode('utf-8')
            return Response(res, content_type='application/json;charset=utf-8', status=200)
        except Exception as e:
            return Response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=505)
