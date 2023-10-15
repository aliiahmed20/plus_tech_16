from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    show_sold_modifier_in_sale_report = fields.Boolean("Show Modifier Sales In Sales Report")
