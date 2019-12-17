# -*- coding: utf-8 -*-
{
    'name': "Bug manage website",

    'summary': """
        Bug manage website""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Saul",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['bm_advanced', 'website', 'website_form'],

    # always loaded
    'data': [
        'data/config_data.xml',
        'views/bug_web.xml',
        'views/bug_extend.xml',
        'views/bug_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}