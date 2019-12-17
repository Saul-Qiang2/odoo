# -*- coding: utf-8 -*-
from odoo import http

# class OdooEcharts(http.Controller):
#     @http.route('/odoo_echarts/odoo_echarts/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_echarts/odoo_echarts/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_echarts.listing', {
#             'root': '/odoo_echarts/odoo_echarts',
#             'objects': http.request.env['odoo_echarts.odoo_echarts'].search([]),
#         })

#     @http.route('/odoo_echarts/odoo_echarts/objects/<model("odoo_echarts.odoo_echarts"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_echarts.object', {
#             'object': obj
#         })