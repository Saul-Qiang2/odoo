# -*- coding: utf-8 -*-
from odoo import http

# class OdooWebLoginBackground(http.Controller):
#     @http.route('/odoo_web_login_background/odoo_web_login_background/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_web_login_background/odoo_web_login_background/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_web_login_background.listing', {
#             'root': '/odoo_web_login_background/odoo_web_login_background',
#             'objects': http.request.env['odoo_web_login_background.odoo_web_login_background'].search([]),
#         })

#     @http.route('/odoo_web_login_background/odoo_web_login_background/objects/<model("odoo_web_login_background.odoo_web_login_background"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_web_login_background.object', {
#             'object': obj
#         })