# -*- coding: utf-8 -*-
#################################################################################
# Author      : Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# Copyright(c): 2015-Present Webkul Software Pvt. Ltd.
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://store.webkul.com/license.html/>
#################################################################################
{
    "name": "POS Order Notes",
    "summary": """Allows the seller to add notes to individual orderlines as well as the complete order in POS.""",
    "category": "Point Of Sale",
    "version": "1.0.0",
    "sequence": 1,
    "author": "Webkul Software Pvt. Ltd.",
    "license": "Other proprietary",
    "website": "https://store.webkul.com/Odoo-POS-Internal-Notes.html",
    "description": """http://webkul.com/blog/odoo-pos-internal-notes/""",
    "live_test_url": "http://odoodemo.webkul.com/?module=pos_order_notes&custom_url=/pos/web/#action=pos.ui",
    "depends": ['point_of_sale'],
    "data": [
        'views/pos_config_view.xml',
    ],
    "assets": {

        'point_of_sale.assets':
            [
                'pos_order_notes/static/src/js/main.js',
                'pos_order_notes/static/src/js/WkAlertPopUp.js',
                'pos_order_notes/static/src/js/WkTextAreaPopUp.js'
            ],
        'web.assets_qweb':
            [
                'pos_order_notes/static/src/xml/pos_order_note.xml',
            ],
    },
    "images": ['static/description/Banner.png'],
    "application": True,
    "installable": True,
    "auto_install": False,
    "price": 35,
    "currency": "USD",
}
