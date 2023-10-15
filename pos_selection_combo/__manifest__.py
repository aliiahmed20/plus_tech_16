# -*- coding: utf-8 -*-
{
    'name': 'POS Selection Combo Pack',
    'author': 'iPredict IT Solutions Pvt. Ltd.',
    'website': 'http://ipredictitsolutions.com',
    "support": "ipredictitsolutions@gmail.com",

    'category': 'Point of Sale',
    'version': '15.0.0.1.1',
    'depends': ['point_of_sale'],

    'data': [
        'security/ir.model.access.csv',
        'views/pos_selection_combo_view.xml',
    ],
    "assets": {

        'point_of_sale.assets':
            [
                'pos_selection_combo/static/src/js/SelectionComboProductItem.js',
                'pos_selection_combo/static/src/js/SelectionComboProductList.js',
                'pos_selection_combo/static/src/js/SelectionComboOrderMenuList.js',
                'pos_selection_combo/static/src/js/ProductSelectionPopup.js',
                'pos_selection_combo/static/src/js/PosSelectionCombo.js',
                'pos_selection_combo/static/src/css/PosSelectionCombo.css'
            ],
        'web.assets_qweb':
            [
                'pos_selection_combo/static/src/xml/Orderline.xml',
                'pos_selection_combo/static/src/xml/WrappedProductNameLines.xml',
                'pos_selection_combo/static/src/xml/ProductItem.xml',
                'pos_selection_combo/static/src/xml/SelectionComboProductItem.xml',
                'pos_selection_combo/static/src/xml/SelectionComboProductList.xml',
                'pos_selection_combo/static/src/xml/SelectionComboOrderMenuList.xml',
                'pos_selection_combo/static/src/xml/ProductSelectionPopup.xml',
            ],
    },


    'license': "OPL-1",
    'price': 149,
    'currency': "EUR",

    "installable": False,

    'images': ['static/description/main.png'],
    'live_test_url': 'https://youtu.be/uf8oWiiO0M8',
}
