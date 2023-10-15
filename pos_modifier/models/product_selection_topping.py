from odoo import api, fields, models, _
from odoo.exceptions import UserError


class ProductExtraTopping(models.Model):
    _name = "product.selection.topping"
    _description = "Product Selection Topping"
    _rec_name = 'description'

    product_template_id = fields.Many2one('product.template', 'Item')
    description = fields.Char('Description', required=True)
    include_price = fields.Boolean('Include Combo Items Price', default=True)
    multi_selection = fields.Boolean("Multiple Selection", default=True)
    product_ids = fields.Many2many('product.product', 'product_tmpl_id', string="Products")
    default_quantity = fields.Float("Default Quantity", default=1, digits='Product Unit of Measure')
    no_of_min_items = fields.Float("Min Items", default="0", digits='Product Unit of Measure')
    no_of_items = fields.Float("Max Items", default="1", digits='Product Unit of Measure')
    product_categ_id = fields.Many2one('pos.category', 'Category')
    include_all = fields.Boolean('Include all Products')

    @api.onchange('include_all')
    def onchange_include_all_products(self):
        if self.include_all:
            if not self.product_categ_id:
                raise UserError(_('Please select Category to include all Product In combo.'))
            self.description = self.product_categ_id.name
            self.product_ids = [(6, 0,
                                 self.env['product.product'].search([('pos_categ_id', '=', self.product_categ_id.id),
                                                                     ('available_in_pos', '=', True)]).ids)]

    @api.onchange('product_categ_id')
    def onchange_product_categ_id(self):
        domain = [('available_in_pos', '=', True)]
        if self.product_categ_id:
            domain.append(('pos_categ_id', '=', self.product_categ_id.id))
        return {'domain': {'product_ids': domain}}
