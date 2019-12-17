# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# @Author  : duq
# @Email   : duquan@bjdvt.com
# @File    :
# @Software: PyCharm Community Edition
# @Description: 请用一句话描述此模块功能

from odoo import api, fields, models
%for obj in object.module_model_1


class ${obj.model_class_name}(models.Model):

    %for model_box in obj.model_relatebox:
    @api.multi
    def ${model_box.related_method_button}(self):
        pass

    % endfor


    _name = '${obj.model_e_name}'
    _description = u'${obj.model_description}'
    _inherit = ['mail.thread',]  # 备注信息轨迹记录

    % for model_line in obj.model_fieldlines:
    % if model_line.fields_name.field_type not in ['group', 'groupend', 'notebook', 'notebookend', 'page', 'pageend', 'tree', 'treeend']:
    % if model_line.fields_name.field_type == 'Selection':
        % if model_line.is_required == True:
    ${model_line.fields_name.field_e_name} = fields.${model_line.fields_name.field_type}(${model_line.fields_name.field_selection}, string=u'${model_line.fields_name.field_c_name}', required=True, track_visibility='onchange')

        % elif model_line.is_readonly == True:
    ${model_line.fields_name.field_e_name} = fields.${model_line.fields_name.field_type}(${model_line.fields_name.field_selection}, string=u'${model_line.fields_name.field_c_name}', readonly=True, track_visibility='onchange')

        % elif model_line.tracking_info == 'always':
    ${model_line.fields_name.field_e_name} = fields.${model_line.fields_name.field_type}(${model_line.fields_name.field_selection}, string=u'${model_line.fields_name.field_c_name}', track_visibility='always')

        % else:
    ${model_line.fields_name.field_e_name} = fields.${model_line.fields_name.field_type}(${model_line.fields_name.field_selection}, string=u'${model_line.fields_name.field_c_name}', track_visibility='onchange')

        % endif
    % elif model_line.fields_name.field_type in ['Many2one', 'Many2many']:
    ${model_line.fields_name.field_e_name} = fields.${model_line.fields_name.field_type}('${model_line.fields_name.field_related_model}', string=u'${model_line.fields_name.field_c_name}')

    % elif model_line.fields_name.field_type == 'One2many':
    ${model_line.fields_name.field_e_name} = fields.${model_line.fields_name.field_type}('${model_line.fields_name.field_related_model}', '${model_line.fields_name.field_one_2_many}', string=u'${model_line.fields_name.field_c_name}')

    % else:
        % if model_line.is_required == True:
    ${model_line.fields_name.field_e_name} = fields.${model_line.fields_name.field_type}(string=u'${model_line.fields_name.field_c_name}', required=True, track_visibility='onchange')

        % elif model_line.is_readonly == True:
    ${model_line.fields_name.field_e_name} = fields.${model_line.fields_name.field_type}(string=u'${model_line.fields_name.field_c_name}', readonly=True, track_visibility='onchange')

        % elif model_line.tracking_info == 'always':
    ${model_line.fields_name.field_e_name} = fields.${model_line.fields_name.field_type}(string=u'${model_line.fields_name.field_c_name}', track_visibility='always')

        % else:
    ${model_line.fields_name.field_e_name} = fields.${model_line.fields_name.field_type}(string=u'${model_line.fields_name.field_c_name}', track_visibility='onchange')

        % endif
    % endif
    % endif
    % endfor


    % if obj.is_status == True:
    state = fields.Selection([
    % for model_bar in obj.show_progress_bar:
        ('${model_bar.selection_key}', '${model_bar.selection_value}'),
    % endfor
    ], string=u'进度条状态', default='${obj.show_progress_bar[0].selection_key}')

    % endif

    %if object.is_upload_file == True:
    upload_files = fields.One2many('${obj.name}.upload.file', 'table', string=u'文件列表')

    %endif

    % for model_bt in obj.model_button:
    @api.multi
    def ${model_bt.button_method_name}(self):
        pass


    % endfor



%if obj.is_upload_file == True:
#  附件上传类
class ${obj.class_name}UploadFile(models.Model):
    # 表名随意
    _name = '${obj.name}.upload.file'

    # 字段固定
    dir_name = fields.Text(u'文件夹名称')
    file_name = fields.Text(u'文件名称')
    file_url = fields.Text(u'文件路径url')
    table = fields.Many2one('${object.name}', string=u'主表id')
    thumbnail_url = fields.Text(u'图片预览url')
    data = fields.Binary(u'预览')
    file_type = fields.Selection([('word', 'word'), ('zip', 'zip'), ('excel', 'excel'), ('file', '通用文档'),
                                  ('pdf', 'pdf'), ('picture', '图片')], string='文件类型', default='file')
%endif
% endfor