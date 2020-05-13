from odoo import api, fields, models,tools

class employee_ext(models.Model):
    _inherit = 'hr.employee'
    
    attendance_id = fields.Char("Attendance ID")
    card_no = fields.Char("Card No " )
    additional_info = fields.Text(string='Additional Info')
