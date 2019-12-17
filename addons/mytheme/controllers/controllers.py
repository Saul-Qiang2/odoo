# -*- coding: utf-8 -*-
from odoo import http

# class Mytheme(http.Controller):
#     @http.route('/mytheme/mytheme/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mytheme/mytheme/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mytheme.listing', {
#             'root': '/mytheme/mytheme',
#             'objects': http.request.env['mytheme.mytheme'].search([]),
#         })

#     @http.route('/mytheme/mytheme/objects/<model("mytheme.mytheme"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mytheme.object', {
#             'object': obj
#         })