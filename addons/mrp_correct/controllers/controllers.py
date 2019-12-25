# -*- coding: utf-8 -*-
from odoo import http

# class MrpCorrect(http.Controller):
#     @http.route('/mrp_correct/mrp_correct/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mrp_correct/mrp_correct/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mrp_correct.listing', {
#             'root': '/mrp_correct/mrp_correct',
#             'objects': http.request.env['mrp_correct.mrp_correct'].search([]),
#         })

#     @http.route('/mrp_correct/mrp_correct/objects/<model("mrp_correct.mrp_correct"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mrp_correct.object', {
#             'object': obj
#         })