# -*- coding: utf-8 -*-
# from odoo import http


# class MabcoReports(http.Controller):
#     @http.route('/mabco_reports/mabco_reports', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mabco_reports/mabco_reports/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mabco_reports.listing', {
#             'root': '/mabco_reports/mabco_reports',
#             'objects': http.request.env['mabco_reports.mabco_reports'].search([]),
#         })

#     @http.route('/mabco_reports/mabco_reports/objects/<model("mabco_reports.mabco_reports"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mabco_reports.object', {
#             'object': obj
#         })
