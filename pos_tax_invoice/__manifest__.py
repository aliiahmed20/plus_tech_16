# -*- coding: utf-8 -*-
{
    'name': "POS tax invoice",
    "version": "15.0.0.2",
    "category": "Accounting",
    'author': "Plus Tech",
    'category': 'accounting',
    'depends': ['base', 'account', 'point_of_sale', 'pos_modifier', 'pos_order_notes'],
    "data": [
        'security/ir.model.access.csv',
    ],
    'qweb': ['static/src/xml/pos.xml'],
    "application": True,
    'assets': {
        'point_of_sale.assets': [
            'pos_tax_invoice/static/src/js/qrcode.js',
            'pos_tax_invoice/static/src/js/pos.js',
            'pos_tax_invoice/static/src/js/JsBarcode.all.min.js',
        ],
        'web.assets_qweb': [
            'pos_tax_invoice/static/src/xml/**/*',
        ],
    },
}
