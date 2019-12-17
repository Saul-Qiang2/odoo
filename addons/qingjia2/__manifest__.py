# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'qingjia2',
    'description': "请假",
    'version': '1.0',
    'category': 'AutoCode Tools',
    'depends': ['base', 'mail',# 'dris_upload',


    ],
    'data': [
        'security/ir.model.access.csv',
        'views/QingJiaDan_view.xml',
        'views/qingjia2_qingjiadan2_inh_view.xml',
    ],
    'auto_install': True,
    'installable': True,
    'application': True,
}