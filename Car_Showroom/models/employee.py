'''
Created on Mar 10, 2020

@author: Khaing Thu Zar
'''
from odoo import api, exceptions, fields, models, _

class Employee(models.Model):
    _name = 'employee.info'
    _description = "Employee"
    
#     _inherit = 'hr.employee'
    
    name = fields.Char("Name", required = True)
#     relate_manager = fields.Many2one('manager.info','Relate Manager')
    phone = fields.Char("Phone")
    address = fields.Char("Address")
    female = fields.Boolean('Female')
    male = fields.Boolean('Male')
    type = fields.Selection([('part_time' , 'Part Time'),
                             ('full time' , 'Full Time')],string ='Type')
    NRC = fields.Char("NRC")
    age = fields.Integer("Age")
#     status = fields.Selection([('current' , 'Current'),
#                                ('aa' , 'AA')] , string = 'Status')
    position = fields.Char("Position")
    
    time_zome = fields.Char("Time Zome")
    job_title = fields.Char("Job Title")
    working_hour = fields.Char("Working Hour")
    
    additional_info = fields.Text(string='Additional Info')