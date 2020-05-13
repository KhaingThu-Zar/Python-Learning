'''
Created on Mar 11, 2020

@author: Khaing Thu Zar
'''

from odoo import api, exceptions, fields, models, _
from odoo.exceptions import RedirectWarning, UserError, ValidationError

class Car_Information(models.Model):
    _name = 'voucher.form'
    _description = "Create Voucher"
    
    type = fields.Char("Car Type")
    customer_name = fields.Char("Customer Name")
    date = fields.Date('Date', required=True)
    price = fields.Float("Price")

    @api.model
    def default_get(self, fields):
        res = super(Car_Information, self).default_get(fields)
        sell_obj = self.env['car.sell'].browse(self.env.context['active_id'])
        if sell_obj.id:
            res['type'] = sell_obj.car_type.name
            res['customer_name'] = sell_obj.customer_name.name
            res['price'] = sell_obj.total
            res['date'] = sell_obj.date
            
        return res
    
    
    @api.multi
    def create_vc(self):
        raise UserError(_("Voucher Create is Successful!..Thanks You!"))

