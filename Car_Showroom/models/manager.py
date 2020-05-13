'''
Created on Mar 10, 2020

@author: Khaing Thu Zar
'''

from odoo import api, exceptions, fields, models, _
from netbios import NRC_ACTSES
class Manager(models.Model):
    
    _name = 'manager.info'
    _description = "Manager Information"
    
    name = fields.Char("Name",required = True)
    NRC = fields.Char("NRC",required = True)
    age = fields.Integer("Age")
    address = fields.Char("Address")
    phone = fields.Char("Phone")
    position = fields.Char("Position")