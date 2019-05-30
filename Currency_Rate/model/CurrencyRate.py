from odoo import models, fields, api
from odoo.exceptions import UserError
class CurrencyRates_umair(models.Model):
    _inherit = "res.currency.rate"


    rate = fields.Float(digits=(12, 10), help='The rate of the currency to the currency of rate 1')  
    
    
    