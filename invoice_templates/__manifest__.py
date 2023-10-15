# -*- coding: utf-8 -*-

{
    'name': 'Invoice Templates',
    'version': '15.0.0.1',
    'category': 'Tools',
    'author': 'Tholol',
    'depends': ['web', 'base', 'account', 'base_vat'],
    'data': [
        "res_company.xml",
        # "invoice_report/external_layout.xml",
        "invoice_report/report_invoice_odoo_standard.xml",
             ],
    'assets': {
        'web.report_assets_common': [
            '/invoice_templates/static/description/src/css/style.css',
        ],
    },
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    "images":['static/description/Banner.png'],
}
