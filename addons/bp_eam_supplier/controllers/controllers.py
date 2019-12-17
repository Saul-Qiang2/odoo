# -*- coding: utf-8 -*-
import json
from odoo import http

class BpEamSupplier(http.Controller):

    # @http.route('/getSupplierCountData/', auth='public')
    # def index1(self, **kw):
    #     return json.dumps({"name":"hddd"})

    @http.route('/getSupplierRatingRate/', auth='public')
    def index(self, **kw):
        return json.dumps({"name":"hddd"})

    # @http.route('/getSupplierRatingTypeRate/', auth='public')
    # def index3(self, **kw):
    #     return json.dumps({"name":"hddd"})
    #
    # @http.route('/getSupplierCooperationCountTop20/', auth='public')
    # def list4(self, **kw):
    #     return json.dumps({"name":"hddd"})
    #
    # @http.route('/getSPCurrentYearCountTop20/', auth='public')
    # def object5(self, obj, **kw):
    #     return json.dumps({"name": "hddd"})
    #
    # @http.route('/getSPCurrentYearBySubctgCountTop20/', auth='public')
    # def index6(self, **kw):
    #     return json.dumps({"name":"hddd"})