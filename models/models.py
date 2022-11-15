# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Conciliacion(models.Model):
    _inherit = 'account.bank.statement.line'
    

    def process_reconciliation(self, counterpart_aml_dicts=None, payment_aml_rec=None, new_aml_dicts=None):
        conciliacion=super(Conciliacion, self).process_reconciliation(counterpart_aml_dicts, payment_aml_rec, new_aml_dicts)        
        if payment_aml_rec:
            payment_aml_rec.write({'statement_line_id': self.id})
            for p in payment_aml_rec:
                # arma la sentencia SQL
                qry = "UPDATE account_move_line SET statement_line_id = {} WHERE id ={}"

                qry=qry.format(self.id,p.id)
                self.env.cr.execute(qry)        
            return payment_aml_rec

    @api.multi
    def button_cancel_reconciliation(self):
        conciliacion=super(Conciliacion, self).button_cancel_reconciliation()        
        for c in self.journal_entry_ids:
            qry = "UPDATE account_move_line SET statement_line_id = null WHERE id ={}"            
            qry=qry.format(c.id)
            self.env.cr.execute(qry)        
        return True