# -*- coding: utf-8 -*-
from odoo import http
# 继承自己编写的控制器
from odoo.addons.bm_website.controllers.main import BmWebsite

class MainExtended(BmWebsite):
    # 无参数，默认使用父类参数
    # 可以在路由中使用占位符来传递参数
    # @http.route(['/hello','/hello/<name>'])
    # 可以用get或者post方法获取参数
    # @http.route()

    # odoo 的提取模型记录的转换器
    @http.route('/hello/<model("res.users"):user>')
    def hello(self, user=None, **kw):
        response = super(MainExtended, self).hello()
        response.qcontext['user'] = user
        return response