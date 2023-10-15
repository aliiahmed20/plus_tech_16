{
    'name': "POS Report Modifier",
    'summary': 'POS Order Report Modifier Fix',
    'depends': ['point_of_sale', 'pos_modifier'],
    'data': [
        'views/product_template_views.xml',
        'views/pos_order_report_views.xml',
    ],
    'installable': True,
    'license': 'LGPL-3',
}
