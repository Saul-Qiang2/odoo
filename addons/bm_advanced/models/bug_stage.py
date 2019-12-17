# -*- coding: utf-8 -*-

from odoo import models, fields, api

class bugStage(models.Model):
    # 要含有模块名称
    _name = 'bm.bug.stage'
    # 模型的标题
    _description = 'bug阶段'
    # 默认的排序字段
    _order = 'sequence, name'
    # 字符串相关类型
    name = fields.Char('名称')
    desc_detail = fields.Text('描述')
    status = fields.Selection([('waiting','未开始'),('doing','进行中'),('cloaed','关闭'),('rework','重测未通过'),],'状态')
    document = fields.Html('文档')
    # 数值相关类型
    sequence = fields.Integer('Sequence')
    #     第一个参数是描述，第二个参数是元组：总位数和小数点精度
    percent_pro = fields.Float('进度', (3, 2))
    # 日期相关类型
    deadline = fields.Date('最晚解决方案')
    create_on = fields.Datetime('创建时间', defualt=lambda self:fields.Datetime.now())
    # 布尔类型
    delay = fields.Boolean('是否延误')
    # 二进制类型
    image = fields.Binary('图片')

    bug_ids = fields.One2many('bm.bug', 'bug_stage_id', string='bug')
