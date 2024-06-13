from odoo import models,api,fields

class Member(models.Model):
    _name = 'hmcoffee.member'
    _description = 'Member'
    _inherit='hmcoffee.manusia'

    jenis_kerja = fields.Selection(string='Jenis Kerja', selection=[('Part-Time', 'Part-Time'), ('Full-Time', 'Full-Time'),])
    lokasi_kerja = fields.Selection(string='Jenis Kerja', selection=[('WFO', 'WFO'), ('WFH', 'WFH'),])
    