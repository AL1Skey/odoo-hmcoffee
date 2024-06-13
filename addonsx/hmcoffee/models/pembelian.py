
from odoo import models, fields, api

class Pembelian(models.Model):
    _name = 'hmcoffee.pembelian'
    _description = 'Pembelian'
    
    nama_supplier = fields.Many2one(comodel_name='hmcoffee.supplier', string="Supplier")  # id
    tgl_pembelian = fields.Date(string='Tanggal Pembelian', default=fields.Datetime.now())
    detail_pembelian = fields.One2many(
        comodel_name='hmcoffee.detail.pembelian',
        inverse_name='pembelian_id',  # Corrected inverse field name
        string="Detail Pembelian"
    )  # list


class DetailPembelian(models.Model):
    _name = 'hmcoffee.detail.pembelian'
    _description = 'DetailPembelian'

    pembelian_id = fields.Many2one(comodel_name='hmcoffee.pembelian', string="Pembelian")  # id
    bahan = fields.Many2many(comodel_name='hmcoffee.produk.bahan', string='Bahan')

    total_pembelian = fields.Integer(compute='_compute_total_pembelian', string='Total Pembelian')
    
    @api.depends('bahan')
    def _compute_total_pembelian(self):
        for data in self:
            data.total_pembelian = sum(produk.harga * produk.stok for produk in data.bahan)
