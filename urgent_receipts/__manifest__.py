# -*- coding: utf-8 -*-
{
    'name': "Urgent Receipts",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management', 'account', 'sale', 'purchase', 'stock', 'product'],

    # always loaded
    'data': [

        'Data/ir_cron.xml',
        'views/purchase_order_views.xml',
        'views/stock_move_views.xml',
        'views/stock_move_line_views.xml',
        'views/purchase_res_config_setting.xml',
        'report/sale_order_report_template_inherit.xml',

    ],
    'installable': True,
    'application': True,
}
