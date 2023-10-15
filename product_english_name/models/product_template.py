from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    english_name = fields.Char('English Name')

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        args = args or []
        recs = self.browse()
        if name:
            recs = self.search((args + ['|', '|', '|', ('english_name', 'ilike', name),
                                        ('barcode', 'ilike', name),
                                        ('default_code', 'ilike', name),
                                        ('name', 'ilike', name)]),
                               limit=limit)
        if not recs:
            recs = self.search([('name', operator, name)] + args, limit=limit)

        return recs.name_get()


class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        args = args or []
        recs = self.browse()
        if name:
            recs = self.search((args + ['|', '|', '|', ('product_tmpl_id.english_name', 'ilike', name),
                                        ('product_tmpl_id.barcode', 'ilike', name),
                                        ('product_tmpl_id.default_code', 'ilike', name),
                                        ('product_tmpl_id.name', 'ilike', name)]),
                               limit=limit)
        if not recs:
            recs = self.search([('name', operator, name)] + args, limit=limit)

        return recs.name_get()
