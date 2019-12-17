# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class BmWebsite(http.Controller):
    @http.route('/hw/', auth='public')
    def hw(self, **kw):
        return ("<h1>Hello, world<h1>")

    @http.route('/hello', auth='public', website=True)
    def hello(self, **kw):
        return request.render("bm_website.hello")

    @http.route('/bugs/', auth='user', website=True)
    def index(self, **kw):
        Bugs = request.env['bm.bug']
        bugs = Bugs.search([])
        return request.render("bm_website.index", {'bugs': bugs})

    @http.route('/bug/<model("bm.bug"):bug>', auth='user', website=True)
    def detail(self, bug, **kw):
        return request.render("bm_website.detail", {'bug': bug})

    @http.route('/bug/add', auth='user', website=True)
    def add(self, **kw):
        users = request.env['res.users'].search([])
        return request.render("bm_website.add", {'users': users})