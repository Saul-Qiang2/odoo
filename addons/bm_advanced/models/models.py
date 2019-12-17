# -*- coding: utf-8 -*-

from odoo import models, fields, api

class bugAdvanced(models.Model):
    # 继承原生模型，没有定义_name模型属性，所以可以使用bm.bug的底层数据库表
    _name = 'bm.bug'
    _inherit = ['bm.bug', 'mail.thread']

    # 新增字段
    time = fields.Integer('所需时间')
    # 给name字段新增help属性
    name = fields.Char(help='简要描述发现的bug')

    bug_stage_id = fields.Many2one('bm.bug.stage', '阶段')
    tag_ids = fields.Many2many('bm.bug.tag', string='标示')
