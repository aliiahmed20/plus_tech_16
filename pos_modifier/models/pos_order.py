from functools import partial
from odoo import fields, models
import uuid


class PosOrder(models.Model):
    _inherit = "pos.order"

    def _order_fields(self, ui_order):
        res = super(PosOrder, self)._order_fields(ui_order)

        process_line = partial(self.env['pos.order.line']._order_own_line_fields,
                               add_own_line=True)
        order_lines = [process_line(ol) for ol in ui_order['lines']] if ui_order['lines'] else False
        new_order_line = []
        if order_lines:
            for order_line in order_lines:
                selection_topping_uuid = uuid.uuid4()
                order_line[2].update({"selection_topping_uuid": selection_topping_uuid})
                if 'own_line' in order_line[2]:
                    own_pro_list = [process_line(ol) for ol in
                                    order_line[2]['own_line']] if order_line[2]['own_line'] else False
                    if own_pro_list:
                        for own in own_pro_list:
                            own[2].update({
                                "parent_uuid": selection_topping_uuid
                            })
                            if own[2]["include_price"]:
                                order_line[2]['price_subtotal'] -= own[2]['price_subtotal']
                                order_line[2]['price_subtotal_incl'] -= own[2]['price_subtotal_incl']
                            else:
                                own[2]['price_unit'] = 0
                                own[2]['price_subtotal'] = 0
                                own[2]['price_subtotal_incl'] = 0
                            new_order_line.append(own)
                new_order_line.append(order_line)
            if new_order_line:
                process_line = partial(self.env['pos.order.line']._order_line_fields, session_id=ui_order['pos_session_id'])
                order_lines = [process_line(ol) for ol in new_order_line]
                res['lines'] = order_lines
        return res


class pos_order_line(models.Model):
    _inherit = "pos.order.line"

    is_selection_combo = fields.Boolean("Selection Combo Line")
    own_ids = fields.One2many("pos.order.line.own", 'orderline_id', "Extra Toppings")
    selection_topping_uuid = fields.Char("UUID")
    parent_uuid = fields.Char("Parent UUID")

    def _order_own_line_fields(self, line, session_id=None, add_own_line=False):
        own_line = []
        if line and 'own_line' in line[2] and add_own_line:
            own_line = line[2]['own_line']
        if "include_price" in line[2]:
            include_price = line[2]["include_price"]
        else:
            include_price = False
        line = super(pos_order_line, self)._order_line_fields(line, session_id=session_id)
        line[2].update({
            "include_price": include_price
        })
        if own_line:
            line[2]['own_line'] = own_line
        return line

    def _order_line_fields(self, line, session_id):
        result = super()._order_line_fields(line, session_id)
        vals = result[2]
        if vals.get('include_price', False):
            vals['include_price'] = line['include_price']
        return result


class pos_order_line_own(models.Model):
    _name = "pos.order.line.own"
    _description = "POS Order Line own"

    orderline_id = fields.Many2one('pos.order.line', 'POS Line')
    product_id = fields.Many2one('product.product', 'Product')
    price = fields.Float('Item Price', required=True)
    qty = fields.Float('Quantity', default='1', required=True)
