# -*- coding: utf-8 -*-
from odoo import http

# class Music-me(http.Controller):
#     @http.route('/music-me/music-me/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/music-me/music-me/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('music-me.listing', {
#             'root': '/music-me/music-me',
#             'objects': http.request.env['music-me.music-me'].search([]),
#         })

#     @http.route('/music-me/music-me/objects/<model("music-me.music-me"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('music-me.object', {
#             'object': obj
#         })