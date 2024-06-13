from odoo import fields, models, api

class Supplier(models.Model):
    _name = 'hmcoffee.supplier'
    _description = 'Supplier Model'
    _rec_name = 'nama'# for labeling many2one

    nama = fields.Char(string='Nama Supplier')
    pic = fields.Char(string='PIC')
    pembelian=fields.One2many(comodel_name='hmcoffee.pembelian',
    inverse_name="nama_supplier",string="Pembelian")
    bahan = fields.Many2many(comodel_name='hmcoffee.produk.bahan', string="Bahan")
