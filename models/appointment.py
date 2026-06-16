# -*- coding: utf-8 -*-
from odoo import models, fields, api

class HiAppointment(models.Model):
    _name = 'hi.appointment'
    _description = 'نموذج المواعيد / Appointment Model'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    patient_id = fields.Many2one('hi.patient', string='المريض / Patient', required=True, tracking=True)
    doctor_name = fields.Char(string='اسم الطبيب / Doctor Name', required=True, tracking=True)
    appointment_date = fields.Datetime(string='تاريخ ووقت الموعد / Appointment Date', required=True, tracking=True)
    
    state = fields.Selection([
        ('draft', 'مسودة / Draft'),
        ('scheduled', 'مجدول / Scheduled'),
        ('checked_in', 'تم الدخول / Checked In'),
        ('completed', 'مكتمل / Completed'),
        ('cancelled', 'ملغي / Cancelled')
    ], string='حالة الموعد / Appointment Status', default='draft', required=True, tracking=True)

    reminder_one_day_sent = fields.Boolean(string='تم إرسال تذكير اليوم السابق / Day Before Reminder Sent', default=False, tracking=True)
    reminder_two_hours_sent = fields.Boolean(string='تم إرسال تذكير الساعتين / Two Hours Reminder Sent', default=False, tracking=True)

    def action_send_sms_simulation(self):
        for record in self:
            # Simulate sending SMS/WhatsApp by posting a message in the chatter
            message = "تم إرسال تنبيه محاكاة لرسالة الجوال/الواتساب للمريض. / SMS/WhatsApp simulation notification sent to patient."
            record.message_post(body=message, message_type='notification')
            
            # For demonstration, we mark reminders as sent
            if not record.reminder_one_day_sent:
                record.reminder_one_day_sent = True
            elif not record.reminder_two_hours_sent:
                record.reminder_two_hours_sent = True
