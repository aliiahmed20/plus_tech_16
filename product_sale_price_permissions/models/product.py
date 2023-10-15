# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    lowest_selling_price = fields.Float(string="Lowest Sale Price")
