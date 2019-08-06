# Copyright 2019 Denis Roussel
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class IrAttachmentCategory(models.Model):

    _name = "ir.attachment.category"
    _inherit = ["ir.attachment.category", "worship.mixin"]
