from odoo import api, fields, models, _


class ProductTemplate(models.Model):
    _inherit = "product.template"

    is_selection_combo = fields.Boolean('Selection Combo', default=False,
                                        help="This will use for Selecting items from Combo Pack")
    product_topping_ids = fields.One2many('product.selection.topping', 'product_template_id', 'Product Toppings')
