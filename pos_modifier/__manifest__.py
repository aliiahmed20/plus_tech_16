# -*- coding: utf-8 -*-
{
    'name': 'POS Modifier',
    'category': 'Point of Sale',
    'version': '15.0.0.1.2',
    'depends': ['point_of_sale', 'nati_arabic_font', 'pos_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/pos_selection_combo_view.xml',
    ],
    "assets": {

        'point_of_sale.assets':
            [
                'pos_modifier/static/src/js/SelectionComboProductItem.js',
                'pos_modifier/static/src/js/SelectionComboProductList.js',
                'pos_modifier/static/src/js/SelectionComboOrderMenuList.js',
                'pos_modifier/static/src/js/ProductSelectionPopup.js',
                'pos_modifier/static/src/js/PosSelectionCombo.js',
                'pos_modifier/static/src/css/PosSelectionCombo.css'
            ],
        'web.assets_qweb':
            [
                'pos_modifier/static/src/xml/Orderline.xml',
                'pos_modifier/static/src/xml/WrappedProductNameLines.xml',
                'pos_modifier/static/src/xml/ProductItem.xml',
                'pos_modifier/static/src/xml/SelectionComboProductItem.xml',
                'pos_modifier/static/src/xml/SelectionComboProductList.xml',
                'pos_modifier/static/src/xml/SelectionComboOrderMenuList.xml',
                'pos_modifier/static/src/xml/ProductSelectionPopup.xml',
            ],
    },
    "installable": True,
    'images': ['static/description/main.png'],
}
