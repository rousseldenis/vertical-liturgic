# Copyright 2019 Denis Roussel
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class IrAttachment(models.Model):

    _name = "ir.attachment"
    _inherit = ["ir.attachment", "worship.mixin"]
