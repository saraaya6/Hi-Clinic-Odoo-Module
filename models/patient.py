# -*- coding: utf-8 -*-
from odoo import models, fields, api

class HiPatient(models.Model):
    _name = 'hi.patient'
    _description = 'نموذج المريض / Patient Model'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='اسم المريض / Patient Name', required=True, tracking=True)
    phone = fields.Char(string='رقم الجوال / Phone Number', tracking=True)
    age = fields.Integer(string='العمر / Age', tracking=True)
    gender = fields.Selection([
        ('male', 'ذكر / Male'),
        ('female', 'أنثى / Female')
    ], string='الجنس / Gender', tracking=True)
    
    appointment_ids = fields.One2many('hi.appointment', 'patient_id', string='المواعيد / Appointments')
    total_stay_time = fields.Float(string='إجمالي وقت البقاء بالدقائق / Total Stay Time (Minutes)', compute='_compute_total_stay_time', store=True)

    @api.depends('appointment_ids', 'appointment_ids.state')
    def _compute_total_stay_time(self):
        for record in self:
            # Placeholder calculation for stay time
            # For a real implementation, we would need check-in and check-out times.
            stay_time = 0.0
            for appt in record.appointment_ids:
                if appt.state == 'completed':
                    stay_time += 30.0 # Assuming 30 minutes per completed appointment
            record.total_stay_time = stay_time
