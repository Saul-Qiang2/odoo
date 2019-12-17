# -*- coding: utf-8 -*-
from odoo import http

class Bug(http.Controller):
    # http.route装饰器定义路径与处理程序的对应关系
    @http.route('/bug_manage')
    def BugManage(self, **kw):
        # 定位到bm.bug
        bugs = http.request.env['bm.bug']
        domain_bug = [('is_closed', '=', False)]
        bugs_open = bugs.search(domain_bug)
        return http.request.render('bug_manage.bugs_template', {
            'bugs_open': bugs_open,
        })