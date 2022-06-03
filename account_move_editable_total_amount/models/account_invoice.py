from odoo import models, fields, api, _
from odoo.exceptions import UserError

class AccountMoveLine(models.Model):
    _inherit = 'account.invoice.line'

    editable_price_total = fields.Float(string="Editable Amount", default=0.0)


    @api.onchange('editable_price_total', 'quantity')
    def onchange_editable_pricetotal(self):
        if self.editable_price_total and self.quantity:
            
            # Remove the selected taxes
            self.invoice_line_tax_ids = None

            # Get the unit price and assign to the related field
            self.price_unit = round(self.editable_price_total/self.quantity, 3)