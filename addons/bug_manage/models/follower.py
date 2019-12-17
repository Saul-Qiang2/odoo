# -*- coding: utf-8 -*-

from odoo import models, fields, api


class follower(models.Model):
    # 继承父类
    _inherit = 'res.partner'
    bug_ids = fields.Many2many('bm.bug', string='bug')

