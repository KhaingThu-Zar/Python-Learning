# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Car ShowRoom',
    'version': '1.0',
    'category': 'Project Management',
    'sequence': 75,
    'summary':'Project Management_1',
    'description': """
ISGM Project Management  System with version 12 community
==========================

This application enables you to manage projects...


You can manage:
---------------
    """,
    'website': '',
    'images': [
      
    ],
    'depends': [
        'hr_expense',
#         'board', 'project', 'sale', 'sale_management', 'hr_expense', 'hr_timesheet',

    ],
    'data': [  
        'security/ir.model.access.csv',
        'views/car_info_view.xml',
        'views/customer_view.xml',
        'views/employee_view.xml',
        'views/manager_view.xml',
        'views/sell_info_view.xml',
        'views/hr_employee_view.xml',
        'views/voucher_form_view.xml',
        'wizards/soldout_report_view.xml',
#         'views/test_base_import.xml',
        'views/base_file_import_templates.xml',
        
    ],
    
    'demo': [],
    'test': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    
    'qweb': [
            'static/src/xml/test_file_import.xml',
#             'static/src/xml/test_import.xml',
             ],
    'js': [
            'static/src/js/file_import_action.js',
            'static/src/js/file_import_button.js',
           
           ],
             
#     
}
