# -*- coding: utf-8 -*-

from odoo import models, fields, api

class bug(models.Model):
    # 类的唯一标识字段，通过此字段引用本类
    _name = 'bm.bug'
    # 提高查询的友好性，标签
    _description = 'bug'

    choice = [('changed', '已修改'),
              ('cannot', '无法修改'),
              ('delay', '推迟'),
              ]
    # 字符字段，属性表示字段必填
    name = fields.Char(string='bug简述', required=True)
    # 文本字段，属性定义长度
    detail = fields.Text(size=150)
    # 布尔字段
    is_closed = fields.Boolean(string='是否关闭')
    # 选择字段
    close_reason = fields.Selection(choice, string='关闭理由')
    # 一个用户对应多个bug
    user_id = fields.Many2one('res.users', string='负责人')
    # 多个关注者对应多个bug
    follower_id = fields.Many2many('res.partner', string='关注者')

    # @api.depends('value')
    # def _value_pc(self):
    #     self.value2 = float(self.value) / 100
    # 装饰器
    @api.multi
    def do_close(self):
        for item in self:
            item.is_closed = True
        return True