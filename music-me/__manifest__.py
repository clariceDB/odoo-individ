# -*- coding: utf-8 -*-
{
    'name': "music-me",

    'summary': """
        Music reccomender""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Clarice",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/music-me_security.xml',
        'views/songs_view.xml',
        'views/artist_view.xml',
        'views/genre_view.xml',
        'views/album_view.xml',
        'views/menu_view.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
}