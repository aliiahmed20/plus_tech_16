# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
import base64
from io import BytesIO

class res_company(models.Model):
    _inherit = "res.company"


    other_name = fields.Char('Indestry')

    po_box = fields.Char('P.O Box')
    small_name = fields.Char('Small name')
    instagram_link = fields.Char('Instagram')

    bank_data = fields.Text('Bank')
    

class account_invoice(models.Model):
    _inherit = "account.move"

    qr_code_base64 = fields.Char("QR Code", store=True) 
    confirmation_datetime = fields.Datetime(string='Confirmation Date', readonly=True, copy=False, store=True)

    def action_post(self):
        super(account_invoice, self).action_post()
        self.write({
                'confirmation_datetime': fields.Datetime.now()
            })

    def generate_qr_code(self):
        
        
        def get_qr_encoding(tag, field):
            company_name_byte_array = field.encode('UTF-8')
            company_name_tag_encoding = tag.to_bytes(length=1, byteorder='big')
            company_name_length_encoding = len(company_name_byte_array).to_bytes(length=1, byteorder='big')
            return company_name_tag_encoding + company_name_length_encoding + company_name_byte_array


        for record in self:
            qr_code_str = ''

            if not record.confirmation_datetime:
                record.confirmation_datetime = record.invoice_date
            seller_name_enc = get_qr_encoding(1, record.company_id.display_name)
            company_vat_enc = get_qr_encoding(2, record.company_id.vat)
            time_sa = fields.Datetime.context_timestamp(self.with_context(tz='Asia/Riyadh'), record.confirmation_datetime).strftime("%Y-%m-%d %H:%M:%S")
            timestamp_enc = get_qr_encoding(3, str(time_sa))
            invoice_total_enc = get_qr_encoding(4, str(record.amount_total))
            total_vat_enc = get_qr_encoding(5, str(record.currency_id.round(record.amount_total - record.amount_untaxed)))

            str_to_encode = seller_name_enc + company_vat_enc + timestamp_enc + invoice_total_enc + total_vat_enc
            qr_code_str = base64.b64encode(str_to_encode).decode('UTF-8')
            record.qr_code_base64 = qr_code_str
