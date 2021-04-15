# -*- coding: utf-8 -*-

{
    'name': 'Odoo Academy',
    
    'summary': """Academy app to manage Training""",
    
    'description': """
        Academy Module to manage Training:
        - Courses
        - Sessions
        - Attendees
    """,
    
    'author': 'Cristian Iñiguez',
    
    'website': 'https://www.cristianiniguez.com',
    
    'category': 'Training',
    'version': '0.1',
    
    'depends': ['base', 'sale_management'],
    
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/academy_course_views.xml',
        'views/academy_session_views.xml',
        'views/sale_order_views.xml',
        'views/product_template_views.xml',
        'wizard/academy_sale_order_create_views.xml'
    ],
    
    'demo': [
        'demo/academy_course_demo.xml',
    ],
}