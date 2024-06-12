from odoo import fields, models, api

class Supplier(models.Model):
    _name = 'hmcoffee.supplier'
    _description = 'Supplier Model'

    nama = fields.Char(string='Nama Supplier')
    pic = fields.Char(string='PIC')
    bahan = fields.Many2many(comodel_name='hmcoffee.produk.bahan', string="Bahan")
