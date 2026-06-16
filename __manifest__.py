# -*- coding: utf-8 -*-
{
    'name': 'العيادة الذكية / Hi Clinic',
    'version': '18.0.1.0.0',
    'category': 'Healthcare',
    'summary': 'إدارة العيادة وكفاءة العمليات / Clinic Management and Operational Efficiency',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/patient_views.xml',
        'views/appointment_views.xml',
        'views/operational_efficiency_views.xml',
        'views/clinic_menus.xml',
    ],
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}