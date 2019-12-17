# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# @Author  : duq
# @Email   : duquan@bjdvt.com
# @File    :
# @Software: PyCharm Community Edition
# @Description: 请用一句话描述此模块功能

from odoo import api, fields, models

class qingjiadan_expansion_inh(models.Model):

    _inherit = 'qingjia.qingjiadan'

    phone = fields.Integer(string=u'请假人电话')