# -*- coding: utf-8 -*-
from odoo import http

# class OpenAcademyv3(http.Controller):
#     @http.route('/open_academyv3/open_academyv3/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/open_academyv3/open_academyv3/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('open_academyv3.listing', {
#             'root': '/open_academyv3/open_academyv3',
#             'objects': http.request.env['open_academyv3.open_academyv3'].search([]),
#         })

#     @http.route('/open_academyv3/open_academyv3/objects/<model("open_academyv3.open_academyv3"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('open_academyv3.object', {
#             'object': obj
#         })