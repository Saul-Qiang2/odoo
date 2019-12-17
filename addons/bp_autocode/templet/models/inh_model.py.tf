# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# @Author  : duq
# @Email   : duquan@bjdvt.com
# @File    :
# @Software: PyCharm Community Edition
# @Description: 请用一句话描述此模块功能

from odoo import api, fields, models

% for raw_m in object.raw_inherit_model
class ${raw_m.ref_inh_class_name}_inh(models.Model):

    _inherit = '${raw_m.addel_field_id.raw_table_model.model}'

    % for inh_field in raw_m.ref_auto_field_name:
        % if inh_field.field_type == 'Selection':
    ${inh_field.field_e_name} = fields.${inh_field.field_type}(${inh_field.fields_selection}, string=u'${inh_field.field_c_name}')
        % elif inh_field.field_type in ['Many2one', 'Many2many']:
    ${inh_field.field_e_name} = fields.${inh_field.field_type}('${inh_field.related_model}', string=u'${inh_field.field_c_name}')
        % elif inh_field.field_type == 'One2many':
    ${inh_field.field_e_name} = fields.${inh_field.field_type}('${inh_field.related_model}', '${inh_field.one_2_many}', string=u'${inh_field.field_c_name}')
        % else:
    ${inh_field.field_e_name} = fields.${inh_field.field_type}(string=u'${inh_field.field_c_name}')
        % endif
    % endfor


    % if raw_m.ref_expr_type == 'button':
    @api.multi
    def ${raw_m.ref_button_new_filed.button_method_name}(self):
        pass
    % endif

% endfor