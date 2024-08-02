from odoo import models, fields, api, _


class ResConfigSetting(models.TransientModel):
    _inherit = 'res.config.settings'

    po_amount = fields.Float(string='Purchase order Amount')

    def set_values(self):
        super(ResConfigSetting, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('urgent_receipts.po_amount', self.po_amount)

    @api.model
    def get_values(self):
        res = super(ResConfigSetting, self).get_values()
        res['po_amount'] = float(
            self.env['ir.config_parameter'].sudo().get_param('urgent_receipts.po_amount', default=0.0))
        return res
