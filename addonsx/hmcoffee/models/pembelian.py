from odoo import models, fields, api

class Pembelian(models.Model):
    _name = 'hmcoffee.pembelian'
    _description = 'Pembelian'

    supplier_id = fields.Many2one(comodel_name='hmcoffee.supplier', string="Supplier")  # id
    tgl_pembelian = fields.Date(string='Tanggal Pembelian', default=fields.Datetime.now())
    detail_pembelian = fields.One2many(
        comodel_name='hmcoffee.detail.pembelian',
        inverse_name='pembelian_id',  # Corrected inverse field name
        string="Detail Pembelian"
    )  # list

    @api.model
    def unlink(self):
        if self.detail_pembelian:
            for data in self.detail_pembelian:
                data.bahan.stok -= data.qty
        return super(Pembelian, self).unlink()

    def write(self, vals):
        for data in self.detail_pembelian:
            data.bahan.stok -= data.qty

        record = super(Pembelian, self).write(vals)

        for data in self.detail_pembelian:
            data.bahan.stok += data.qty

        return record

class DetailPembelian(models.Model):
    _name = 'hmcoffee.detail.pembelian'
    _description = 'Detail Pembelian'

    pembelian_id = fields.Many2one(comodel_name='hmcoffee.pembelian', string="Pembelian")  # id
    bahan = fields.Many2one(comodel_name='hmcoffee.produk.bahan', string='Bahan')
    qty = fields.Integer(string='Quantity')
    total_pembelian = fields.Integer(compute='_compute_total_pembelian', string='Total Pembelian')

    @api.depends('bahan', 'qty')
    def _compute_total_pembelian(self):
        for data in self:
            data.total_pembelian = data.bahan.harga * data.qty
