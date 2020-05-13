'''
Created on Mar 11, 2020

@author: Khaing Thu Zar
'''

import random
from io import BytesIO
from datetime import date, timedelta as td
from datetime import datetime
import datetime
from base64 import decodestring
import base64
from odoo.exceptions import UserError
from odoo import models, fields, api, _
from calendar import month_name
from imp import new_module
from _ast import Str 
import pytz
import string
import logging
from xlutils.filter import XLWTWriter
_logger = logging.getLogger(__name__)

try:
    import xlwt
    from xlwt import *
except ImportError:
    xlwt = None
import logging
_logger = logging.getLogger(__name__)


class Car_Information(models.Model):
    _name = 'sold.out.info'
    _description = "Sold Out Information"
    
    from_date = fields.Date("From Date", required=True)
    to_date = fields.Date("To Date", required=True)
    datas = fields.Binary('File')
    
    
    @api.multi      
    def soldout_report(self):
        workbook = xlwt.Workbook()
        worksheet = workbook.add_sheet('Soldout Data', cell_overwrite_ok=True)
        
        xlwt.add_palette_colour("custom_colour", 0x21)
        workbook.set_colour_RGB(0x21, 252, 228, 214)
          
        xlwt.add_palette_colour("green_color", 0x11)
        workbook.set_colour_RGB(0x11 , 98, 167, 59)      
        xlwt.add_palette_colour("yellow_color", 0x22)
        workbook.set_colour_RGB(0x22 , 255, 251, 204)
       
        num_format_str = '$#,##0.00' 
        
        borders = Borders()
        borders.left, borders.right, borders.top, borders.bottom = Borders.DOTTED, Borders.DOTTED, Borders.DOTTED, Borders.DOTTED
        heading_center_style = xlwt.easyxf("font:bold on, height 320; pattern: pattern solid, pattern_fore_colour green_color; alignment: horizontal left,vertical center")
        heading_style = xlwt.easyxf("font:bold on, height 260; pattern: pattern solid, pattern_fore_colour orange; alignment: horizontal center,vertical center;borders:left dotted,right dotted,top dotted,bottom dotted")
        no_style = xlwt.easyxf("font: height 240; pattern: fore_colour white; alignment: horizontal center,vertical center;borders:left dotted,right dotted,top dotted,bottom dotted")
        data_style = xlwt.easyxf("font: height 240; pattern: pattern solid; alignment: horizontal center,vertical center;borders:left dotted,right dotted,top dotted,bottom dotted")
        total_data_style = xlwt.easyxf("font: height 240; pattern: pattern solid, pattern_fore_colour yellow_color; alignment: horizontal center,vertical center;borders:left dotted,right dotted,top dotted,bottom dotted")
        amount_style = xlwt.easyxf("font: height 240; pattern: pattern solid; alignment: horizontal right,vertical center;borders:left dotted,right dotted,top dotted,bottom dotted")
        master_data_style = xlwt.easyxf("font: height 240; pattern: fore_colour red; alignment: horizontal center,vertical center;borders:left dotted,right dotted,top dotted,bottom dotted")
        master_amount_style = xlwt.easyxf("font: height 240; pattern: fore_colour red; alignment: horizontal right,vertical center;borders:left dotted,right dotted,top dotted,bottom dotted")
         
        def get_width(num_characters):
            return int((1 + num_characters) * 256)
        
#         worksheet.panes_frozen = True
#         worksheet.remove_splitsproject = True
#         worksheet.horz_split_pos = 3
        
        worksheet.col(0).width = get_width(15)
        worksheet.col(1).width = get_width(20)
        worksheet.col(2).width = get_width(20)
        worksheet.col(3).width = get_width(20)
        worksheet.col(4).width = get_width(20)
        worksheet.col(5).width = get_width(20)
        worksheet.col(6).width = get_width(20)
        worksheet.col(7).width = get_width(20)
        worksheet.col(8).width = get_width(20)
        worksheet.col(9).width = get_width(20)
        
        heading__row_cust = 0
        heading__row_cust1 = 1
        worksheet.write_merge(heading__row_cust, heading__row_cust1, 0, 9, ' Car Sold Out Report ', heading_center_style)

        # header in excel file
        heading_row = 2
        heading_col = 0
        headings = ['No', 'Date', 'Car Type', 'Price', 'Colour', 'Tax', 'Total Amount', 'Manager Name', 'Employee Name', 'Customer Name']
 
        for heading in headings:
#             worksheet.write(heading_row,heading_col, heading, heading_style)#work in excel file
            worksheet.write(heading_row, heading_col, heading, heading_style)
            heading_col += 1
        
        report_line_row = 3
        report_line_col = 0
        row_no = 1
        
        sell_id =self.env['car.sell'].search([('date', '>=', self.from_date),('date', '<=', self.to_date),('state', '=', 'sold')])
        
        if sell_id:
            for sell_data in sell_id:
                worksheet.write(report_line_row, report_line_col, row_no, no_style)
                report_line_col += 1
                
    #           ********  For Date
                if sell_data.date is not False:
                    worksheet.write(report_line_row, report_line_col,str(sell_data.date), master_data_style)   
                else:
                    worksheet.write(report_line_row, report_line_col, '', master_data_style)   
                report_line_col += 1
                
    #             For Car Type ******
                if sell_data.car_type.name is not False:
                    worksheet.write(report_line_row, report_line_col,sell_data.car_type.name, master_data_style)   
                else:
                    worksheet.write(report_line_row, report_line_col, '', master_data_style)   
                report_line_col += 1
                
    #             For Price *********
                if sell_data.price is not False:
                    worksheet.write(report_line_row, report_line_col,sell_data.price, master_data_style)   
                else:
                    worksheet.write(report_line_row, report_line_col, '', master_data_style)   
                report_line_col += 1
                
    #             For Colour*********
                if sell_data.colour is not False:
                    worksheet.write(report_line_row, report_line_col,sell_data.colour, master_data_style)   
                else:
                    worksheet.write(report_line_row, report_line_col, '', master_data_style)   
                report_line_col += 1
                
                #             For Tax*********
                if sell_data.tax is not False:
                    worksheet.write(report_line_row, report_line_col,sell_data.tax, master_data_style)   
                else:
                    worksheet.write(report_line_row, report_line_col, '', master_data_style)   
                report_line_col += 1
                
                #             For Tax amount*********
                if sell_data.tax_amount is not False:
                    worksheet.write(report_line_row, report_line_col,sell_data.tax_amount, master_data_style)   
                else:
                    worksheet.write(report_line_row, report_line_col, '', master_data_style)   
                report_line_col += 1
                
                #             For Manager Name*********
                if sell_data.manager_name.name is not False:
                    worksheet.write(report_line_row, report_line_col,sell_data.manager_name.name, master_data_style)   
                else:
                    worksheet.write(report_line_row, report_line_col, '', master_data_style)   
                report_line_col += 1
                
                #             For Employee Name*********
                if sell_data.employee_name.name is not False:
                    worksheet.write(report_line_row, report_line_col,sell_data.employee_name.name, master_data_style)   
                else:
                    worksheet.write(report_line_row, report_line_col, '', master_data_style)   
                report_line_col += 1
                
                #             For Customer Name*********
                if sell_data.customer_name.name is not False:
                    worksheet.write(report_line_row, report_line_col,sell_data.customer_name.name, master_data_style)   
                else:
                    worksheet.write(report_line_row, report_line_col, '', master_data_style)   
                report_line_col += 1
                
                row_no += 1
                report_line_row += 1
                report_line_col = 0
            
            
#                 
        fp = BytesIO()
        workbook.save(fp)
        fp.seek(0)
        stock_file = base64.encodestring(fp.read())
        self.write({'datas':stock_file})
        fp.close()
        return {
            'type' : 'ir.actions.act_url',
            'url':   '/web/binary/download_car_soldout_report?&model=%s&id=%s&filename=Car Soldout Report.xls' % (self, self.id),
            'target': 'new',
            }
    
