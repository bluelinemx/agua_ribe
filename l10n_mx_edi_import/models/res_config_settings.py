# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class ResCompany(models.Model):
    _inherit = "res.company"

    l10n_mx_edi_import_pue_payment_term_id = fields.Many2one(comodel_name='account.payment.term',
                                                             string='PUE Payment Term')
    l10n_mx_edi_import_ppd_payment_term_id = fields.Many2one(comodel_name='account.payment.term',
                                                             string='PPD Payment Term')


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    l10n_mx_edi_import_pue_payment_term_id = fields.Many2one(comodel_name='account.payment.term',
                                                             related='company_id.l10n_mx_edi_import_pue_payment_term_id',
                                                             string='PUE Payment Term')
    l10n_mx_edi_import_ppd_payment_term_id = fields.Many2one(comodel_name='account.payment.term',
                                                             related='company_id.l10n_mx_edi_import_ppd_payment_term_id',
                                                             string='PPD Payment Term')
