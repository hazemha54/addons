# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class price_unit_float3(models.Model):
#     _name = 'price_unit_float3.price_unit_float3'
#     _description = 'price_unit_float3.price_unit_float3'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
