# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class EchartBuilder(http.Controller):
    @http.route('/eb_index', type='http', auth="user", website=True)
    def index(self, **kw):
        return request.render('echart_builder.index')
