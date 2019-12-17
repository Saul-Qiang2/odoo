# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Bug(models.Model):
    _inherit = 'bm.bug'

    @api.model
    def website_form_input_filter(self, request, values):
        if values.get('name'):
            values['name'] = values['name'].strip()
            if len(values['name']) < 3:
                raise ValidationError(
                    '名称长度不可少于三个字符'
                )
        return values