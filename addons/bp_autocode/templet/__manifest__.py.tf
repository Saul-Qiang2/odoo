# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': '${object.module_e_name}',
    'description': "${object.module_c_name}",
    'version': '1.0',
    'category': 'AutoCode Tools',
    'depends': ['base', 'mail',
    % for mu in object.rely_module:
       '${mu.rely_module_ename}',
    % endfor

    % for raw_m in object.raw_inherit_model
        '${raw_m.addel_field_id.raw_table_model.model}',
    % endfor
    ],
    'data': [
        'security/ir.model.access.csv',
      % if object.module_model_1
        'views/view.xml',
      % endif
      % if object.raw_inherit_model
        'views/inh_view.xml',
      % endif
    ],
    # 自动安装：当依赖（depends）安装完毕后，自动安装本模块，这里设置为否
    'auto_install': False,
    # 是否可安装：设置为false，从前端搜索不到本模块
    'installable': True,
    # 是否是应用类型：true：可以在筛选器中用“应用”进行筛选
    'application': True,
}

