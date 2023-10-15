from odoo import api, models, _
from odoo.exceptions import ValidationError, UserError


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.onchange('price_unit', 'discount')
    @api.constrains('price_unit', 'discount')
    def _check_product_price(self):
        """
        prevent sales person from selling product with less than authorized price
        :return: None
        """
        current_user = self.env.user
        for line in self:
            price = line.price_unit - ((line.price_unit * line.discount) / 100)
            if line.price_unit:
                if current_user.has_group('product_sale_price_permissions.group_prevent_selling_below_sale_price'):
                    if price < line.product_id.list_price:
                        raise ValidationError(
                            _("Price Unit Must be greater than product sale price product sale price is") + " %s " % (
                                line.product_id.list_price))

                elif current_user.has_group('product_sale_price_permissions.group_lowest_selling_price'):
                    if price < line.product_id.lowest_selling_price:
                        raise ValidationError(_("Price Unit Must be greater than Lowest Sale Price\n"
                                                "Lowest sale price is") + " %s" % line.product_id.lowest_selling_price)

                else:
                    if price < line.product_id.lowest_selling_price:
                        ss = {
                            'title': _('Warning'),
                            'message': _('Selling price lower than lowest selling price'),
                        }
                        return {'warning': ss}
