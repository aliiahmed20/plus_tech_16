# -*- coding: utf-8 -*-
#################################################################################
# Author      : Plus Tech.
# Copyright(c): 2021-Present Plus Tech IT Solutions.
# All Rights Reserved.
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <www.plustech.com/license>
#################################################################################

{
    'name': "Product Sale Price Permission",

    'summary': "add less sale price , control sale price",

    'author': "Plus Tech",
    'website': "",

    'category': 'Extra Tools',
    'version': '1.0',

    'depends': ['product', 'account', 'sale', 'base'],

    'data': [
        'security/sale_security.xml',
        'views/product.xml',
    ],
    'images': [],

    'license ': 'LGPL-3',

    'installable': True,
    'auto_install': False,
    'application': True,
}
