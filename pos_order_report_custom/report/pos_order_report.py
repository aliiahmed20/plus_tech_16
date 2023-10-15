from odoo import models, fields


class PosOrderReport(models.Model):
    _inherit = "report.pos.order"
    show_sold_modifier_in_sale_report = fields.Boolean()
    parent_uuid = fields.Char()

    def _select(self):
        return super(PosOrderReport, self)._select() +\
               ',pt.show_sold_modifier_in_sale_report AS show_sold_modifier_in_sale_report, ' \
               'l.parent_uuid AS parent_uuid'

    def _group_by(self):
        return super(PosOrderReport, self)._group_by() + \
               ',pt.show_sold_modifier_in_sale_report, l.parent_uuid'
