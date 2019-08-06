# Copyright 2019 Denis Roussel
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Worship Event',
    'summary': """
        Adds worship event management""",
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Denis Roussel,Odoo Community Association (OCA)',
    'depends': [
        "worship",
        "event"
    ],
    'data': [
        'views/event_event.xml',
    ],
    'demo': [
    ],
}
