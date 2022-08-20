# -*- coding: utf-8 -*-
{
    'name': "Fleet Logs",

    'summary': """
        Fleet logs like Odoo 13""",

    'description': """
        Fleet logs like Odoo 13
    """,

    'author': "Exemax",
    'website': "http://www.exemax.com.ar",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Fleet',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'fleet'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/fleet_fuel.xml',
        #'views/fleet_service.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
