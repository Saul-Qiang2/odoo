# -*- coding: utf-8 -*-
from odoo import http

# class BmAdvanced(http.Controller):
#     @http.route('/bm_advanced/bm_advanced/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bm_advanced/bm_advanced/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bm_advanced.listing', {
#             'root': '/bm_advanced/bm_advanced',
#             'objects': http.request.env['bm_advanced.bm_advanced'].search([]),
#         })

#     @http.route('/bm_advanced/bm_advanced/objects/<model("bm_advanced.bm_advanced"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bm_advanced.object', {
#             'object': obj
#         })