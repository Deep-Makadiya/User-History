# -*- coding: utf-8 -*-
{
    'name': "User History",

    'summary': "Check the History of the USer",

    'description': """
In this model When we make any changes into the settings of the users than that changes ,
like which user is changed that,old values,new values,group name ,modification user id 
all will be there in the submenu which is maded uner the user & companies.
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

        'security/ir.model.access.csv',
        'views/user_history_views.xml',


    ],
    'installable': True,
    'application': True,
}
