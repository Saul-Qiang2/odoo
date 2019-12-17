# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'qingjia_expansion',
    'description': "请假单扩展",
    'version': '1.0',
    'category': 'AutoCode Tools',
    'depends': ['base', 'mail',# 'dris_upload',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/qingjiadan_expansion_inh_view.xml',
    ],
    'auto_install': True,
    'installable': True,
    'application': True,
}