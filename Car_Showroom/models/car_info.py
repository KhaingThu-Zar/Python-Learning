'''
Created on Mar 10, 2020

@author: Khaing Thu Zar
'''
from odoo import api, exceptions, fields, models,_

class Car_Information(models.Model):
    _name = 'car.info'
    _description = "Car Information"
    
    name = fields.Char("Type", required = True)
    car_colour = fields.Char("Colour", required = True)
    engine = fields.Char("Engine")
    car_price = fields.Integer("Price")
    
    
class Class_name(models.Model):
    _name='model.name'    
    @api.multi
    def unlink(self,values):
        
    ## Write Code with condition ####
        campus_unlink = super(Class_name,self).unlink()
        return campus_unlink
    
    
    