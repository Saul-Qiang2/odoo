# -*- coding: utf-8 -*-
{
    'name': 'My Library',
    'summary': '轻松管理图书',
    'description': """长描述占位""",
    'author': 'Alan Hou',
    'website': 'https://alanhou.org',
    'category': 'Uncategorized',
    'version': '12.0.1',
    'depends': ['base', 'website'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/snippets.xml',
        'views/library_book.xml',

    ],
    'application': True,
}