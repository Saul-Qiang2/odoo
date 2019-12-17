# -*- coding: utf-8 -*-
{
    'name': "bug wizard",

    'summary': """
        bug 管理辅助使用模块""",

    'description': """
        bug 管理辅助使用模块
    """,

    'author': "Saul",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'bug_manage'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/bug_wizard.xml',
    ],
    # only loaded in demonstration mode
    'application': True,
}