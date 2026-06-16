# -*- coding: utf-8 -*-
from odoo import models, fields


class HiOperationalEfficiency(models.Model):
    _name = 'hi.operational.efficiency'
    _description = 'نموذج كفاءة العمليات والتحسين / Operational Efficiency Model'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='عنوان التقرير / Report Title', required=True, tracking=True)
    
    efficiency_type = fields.Selection([
        ('waiting_time', 'وقت انتظار / Waiting Time'),
        ('material_waste', 'هدر مواد / Material Waste'),
        ('overprocessing', 'حركات زائدة / Overprocessing')
    ], string='تصنيف الهدر / Waste Category', required=True, tracking=True)

    estimated_loss = fields.Float(string='الخسارة المالية التقديرية (ريال) / Estimated Financial Loss (SAR)', tracking=True)
    improvement_log = fields.Text(string='سجل حل المشكلة والتحسين / Continuous Improvement Log', tracking=True)
    
    state = fields.Selection([
        ('draft', 'مسودة / Draft'),
        ('review', 'تحت المراجعة / Under Review'),
        ('implemented', 'مطبق / Implemented')
    ], string='حالة التطبيق / Implementation State', default='draft', required=True, tracking=True)
