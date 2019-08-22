# -*- coding: utf-8 -*-
from odoo import http

# class Musictwo(http.Controller):
#     @http.route('/musictwo/musictwo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/musictwo/musictwo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('musictwo.listing', {
#             'root': '/musictwo/musictwo',
#             'objects': http.request.env['musictwo.musictwo'].search([]),
#         })

#     @http.route('/musictwo/musictwo/objects/<model("musictwo.musictwo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('musictwo.object', {
#             'object': obj
#         })