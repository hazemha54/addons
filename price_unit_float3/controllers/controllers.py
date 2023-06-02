# -*- coding: utf-8 -*-
# from odoo import http


# class PriceUnitFloat3(http.Controller):
#     @http.route('/price_unit_float3/price_unit_float3/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/price_unit_float3/price_unit_float3/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('price_unit_float3.listing', {
#             'root': '/price_unit_float3/price_unit_float3',
#             'objects': http.request.env['price_unit_float3.price_unit_float3'].search([]),
#         })

#     @http.route('/price_unit_float3/price_unit_float3/objects/<model("price_unit_float3.price_unit_float3"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('price_unit_float3.object', {
#             'object': obj
#         })
