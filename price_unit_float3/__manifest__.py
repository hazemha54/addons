# -*- coding: utf-8 -*-
{
    'name': "price_unit_float3",

    'summary': """
       print price unit with 3 number after decimal point""",

    'description': """
        print price unit 3 number after decimal point
    """,
    'author': "Infotech Consulting Services - ICS",
    'website': "http://www.ics-tn.com",
    'category': 'Uncategorized',
    'version': '13.0.0.0.1',
    'depends': ['base','sale','purchase','account','delivery_report_extend_last'],
    'data': [
        'views/sale_order_report.xml',
        'views/purchase_order_report.xml',
        'views/acount_move_report.xml',
    ],
}
