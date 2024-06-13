from odoo import models,fields,api

class Manusia(models.Model):
    _name = 'hmcoffee.manusia'
    _description = 'Manusia'

    nama = fields.Char(string='Nama')
    usia = fields.Integer(string='Usia')
    gender = fields.Selection(string='Gender', selection=[('Pria', 'Pria'), ('Wanita', 'Wanita'),])
    
    
