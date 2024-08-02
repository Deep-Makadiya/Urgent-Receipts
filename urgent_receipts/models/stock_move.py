from odoo import models, fields, api, _


class StockMove(models.Model):
    _inherit = 'stock.move'

    urgent_move = fields.Boolean(string="Urgent Move")

    @api.model
    def cron_urgent_receipts(self):
        pickings = self.env['stock.picking'].search([])
        for picking in pickings:
            if any(line.urgent_move == 1 and picking.priority == '0' for line in picking.move_ids_without_package):
                picking.write({'priority': '1'})
                print("picking.priority>>>>>>>>>>>>>>>>>>", picking.priority)
            if all(line.urgent_move == 0 and picking.priority == '1' for line in picking.move_ids_without_package):
                picking.write({'priority': '0'})
                print("picking.priority ??????????????????????", picking.priority)

    def _prepare_move_line_vals(self, quantity=None, reserved_quant=None):
        self.ensure_one()
        res = super()._prepare_move_line_vals(quantity, reserved_quant)
        res['urgent_move_line'] = self.urgent_move if self.urgent_move else False

        return res


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    urgent_move_line = fields.Boolean(string="Urgent Move Line")
