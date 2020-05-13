'''
Created on Mar 10, 2020

@author: Khaing Thu Zar
'''
from odoo import api, exceptions, fields, models,_

class Car_Information(models.Model):
    _name = 'cus.info'
    _description = "Customer Information"
    
    name = fields.Char("Customer Name", required = True)
    nrc = fields.Char("NRC_No", required = True)
    phone = fields.Char("Phone No", required = True)
    age = fields.Integer("Age")
    address = fields.Char("Address")
    gender = fields.Selection([('male', 'Male'),
                              ('female', 'Female'),
                              ], string='Gender')