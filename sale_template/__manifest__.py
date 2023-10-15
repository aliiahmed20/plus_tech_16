# -*- coding: utf-8 -*-
{
    'name': "Sale  Order Templates",

    'summary': """
        SO  Templates
       """,

    'description': """
        Custom Sale order and Qutation
    """,

    'author': "Plus Tech",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'sale',
    'version': '0.3',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],
    'assets': {
        'web.report_assets_common': [
            '/sale_template/static/description/src/css/style.css',
        ],
    },
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/sale_order_temp.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
