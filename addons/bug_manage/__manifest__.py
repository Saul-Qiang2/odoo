# -*- coding: utf-8 -*-
{
    # 模块名字
    'name': "bug 管理",

    # 模块简介
    'summary': """
        用于软件开发过程中 bug 的管理""",

    # 模块描述
    'description': """
        用于软件开发过程中 bug 的管理
    """,

    'author': "Saul",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    # 添加依赖的其他模块
    'depends': ['base'],

    # always loaded 视图文件
    'data': [
        'security/ir.model.access.csv',
        'demo/demo.xml',
        'views/bugs_template.xml',
        'views/bugs.xml',
        'views/follower.xml',

    ],
    # only loaded in demonstration mode
    # 加载演示数据

    'qweb': [

    ],
    'application': True
}