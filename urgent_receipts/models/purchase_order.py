from odoo import models, fields, api, _
import warnings


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.model
    def create(self, vals):
        order = super(PurchaseOrder, self).create(vals)
        setting_po_amount = float(
            self.env['ir.config_parameter'].sudo().get_param('urgent_receipts.po_amount',
                                                             default=0.0))

        if setting_po_amount and order['amount_total'] != 0.0 and setting_po_amount > order['amount_total']:
            order.button_confirm()

        return order

    def button_confirm(self):
        res = super(PurchaseOrder, self).button_confirm()

        setting_po_amount = float(
            self.env['ir.config_parameter'].sudo().get_param('urgent_receipts.po_amount',
                                                             default=0.0))

        if setting_po_amount and self.amount_total != 0.0 and setting_po_amount < self.amount_total:
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': _(
                        'Your setting PO Amount:%f is less than the Current Amount Total:%f', setting_po_amount,
                        self.amount_total),
                    'type': 'warning',
                    'sticky': True,  # True/False will display for few seconds if false
                    'next': {'type': 'ir.actions.act_window_close'},
                }
            }
        return res


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    urgent_order_line = fields.Boolean(string="Urgent Order Line")

    @api.model
    def _prepare_stock_move_vals(self, picking, price_unit, product_uom_qty, product_uom, order_line=None):
        res = super(PurchaseOrderLine, self)._prepare_stock_move_vals(
            picking, price_unit, product_uom_qty, product_uom
        )
        res['urgent_move'] = self.urgent_order_line if self.urgent_order_line else False

        return res
