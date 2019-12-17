# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# @Author  : duq
# @Email   : duquan@bjdvt.com
# @File    :
# @Software: PyCharm Community Edition
# @Description: 请用一句话描述此模块功能

from odoo import api, fields, models

class QingJiaDan(models.Model):

    @api.multi
    def do_confirm(self):
        pass

    @api.multi
    def do_complete(self):
        pass

    _name = 'qingjia2.qingjiadan'
    _description = u'请假单'
    _inherit = ['mail.thread',]  # 备注信息轨迹记录

    name = fields.Char(string=u'姓名', required=True, track_visibility='onchange')

    days = fields.Integer(string=u'请假天数', required=True, track_visibility='onchange')

    starttime = fields.Date(string=u'开始日期', required=True, track_visibility='onchange')

    reason = fields.Text(string=u'请假事由', track_visibility='onchange')

    state = fields.Selection([
        ('draft', '草稿'),
        ('confirm', '待审批'),
        ('complete', '已完成'),
    ], string=u'进度条状态', default='draft')

    @api.multi
    def do_confirm(self):
        pass


    @api.multi
    def do_complete(self):
        pass