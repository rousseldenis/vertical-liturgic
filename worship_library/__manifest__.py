# Copyright 2019 Denis Roussel
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Worship Library',
    'summary': """
        Adds base worship module to manage library""",
    'version': '13.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'ACSONE SA/NV,Odoo Community Association (OCA)',
    'depends': [
        "worship",
        "attachment_category",
    ],
    'data': [
        'views/ir_attachment.xml',
    ],
    'demo': [
    ],
}
