# -*- coding: utf-8 -*-
# © 2016 Gonzalo Borras gborras@bisnesmart.com
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp import models, fields, api, exceptions


class account_invoice(models.Model):
    _inherit = 'account.invoice'

    @api.model
    def create(self,data):
        """
        Override the field user_id when create invoice
        """
        data['user_id']=self.env.user.id
        return super(account_invoice,self).create(data)
