from odoo import fields, models, api

class Supplier(models.Model):
    _name = 'hmcoffee.supplier'
    _description = 'Supplier Model'
    # _rec_name = 'nama'# for labeling many2one

    name = fields.Char(string='Nama Supplier')
    pic = fields.Char(string='PIC')
    pembelian_ids=fields.One2many(comodel_name='hmcoffee.pembelian',
    inverse_name="supplier_id",string="Pembelian")
    bahan_ids = fields.Many2many(comodel_name='hmcoffee.produk.bahan', string="Bahan")
