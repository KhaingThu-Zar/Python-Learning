'''
Created on Mar 10, 2020

@author: Khaing Thu Zar
'''
from odoo import api, exceptions, fields, models, _


class CarShow(models.Model):
    _name = 'car.sell'
    _description = 'Car Sell Info'
    _rec_name = "car_type"

    date = fields.Date('Date', required=True, copy=False)
    manager_name = fields.Many2one('manager.info', string="Manager Name")
    employee_name = fields.Many2one('employee.info', string="Employee Name")
#     employee_name = fields.Many2many('employee.info','employee_info_show','emp_id','emp_show_id',string="Employee Name")
    customer_name = fields.Many2one('cus.info', string="Customer Name")
    car_type = fields.Many2one('car.info', string="Car Type")
    price = fields.Float("Price")
    colour = fields.Char("Colour")
    tax = fields.Float("Tax")
    tax_amount = fields.Float("Tax Amount",readonly=True)
    quantity = fields.Integer("Quantity")
    total = fields.Float("Total Amount", readonly=True)
    
    state = fields.Selection([('show', 'Show'),
                              ('sold', 'Sold Out'),
                              ('cancel', 'Cancel')
                              ], string='Status')
    
    specification = fields.Char("Specification")
    
#     car_type = fields.Many2many('car.info','car_info_show','car_id','show_id',string="Car Type")
    
#     ****** Onchange Method depend on car_type field *********
    @api.onchange('car_type')
    def _get_price(self):
        car_id = self.env['car.info'].search([('id', '=' , self.car_type.id)])
        self.price = car_id.car_price
        self.colour = car_id.car_colour
        
        
    @api.onchange('tax','quantity','price')
    def _get_tax_amount(self):
#         car_id = self.env['car.info'].search([('id', '=' , self.car_type.id)])
        amount = self.quantity * self.price
        self.tax_amount = (amount * self.tax) * 0.01
        self.total = amount + self.tax_amount
        
        
    @api.multi
    def sell_car(self):
        self.write({'state': 'sold'})    
        
    @api.multi
    def create_voucher(self):
        print("Voucher") 
        
        return {
            'type': 'ir.actions.act_window',
            'name': 'Voucher',
            'res_model': 'voucher.form',
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
          }
        
    @api.model
    def create(self, vals):
        # Do your custom logic here
        if 'quantity' in vals:
            amount = vals.get('quantity') * vals.get('price') 
            vals['tax_amount'] = (amount * vals.get('tax')) * 0.01
            vals['total'] = amount + vals.get('tax_amount')
        else:
            vals['tax_amount'] = (vals.get('price') * vals.get('tax')) * 0.01
            vals['total'] = vals.get('price') + vals.get('tax_amount')
        return super(CarShow, self).create(vals)
    
    @api.multi
    def write(self, vals):
        # Do your custom logic here
        if 'quantity' in vals:
            amount = vals.get('quantity', self.quantity) * vals.get('price', self.price) 
            vals['tax_amount'] = (amount * vals.get('tax', self.tax)) * 0.01
            vals['total'] = amount + vals.get('tax_amount', self.tax_amount)
        else:
            vals['tax_amount'] = (vals.get('price', self.price) * vals.get('tax', self.tax)) * 0.01
            vals['total'] = vals.get('price', self.price) + vals.get('tax_amount', self.tax_amount)
        return super(CarShow, self).write(vals)
