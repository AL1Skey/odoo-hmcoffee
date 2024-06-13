from odoo import api,models,fields

class Produk(models.Model):
    _name = "hmcoffee.produk"
    _description = "model.technical.name"
    
    produk_id = fields.Many2one(comodel_name="hmcoffee.pesanan",string="product_id")
    nama = fields.Char(string="Nama Produk")
    bahan = fields.One2many(comodel_name="hmcoffee.produk.bahan",inverse_name="bahan_id", string="Bahan",required=True)
    harga = fields.Float(readonly=True, string="Harga", compute="_compute_harga")
    kategori = fields.Selection(selection=[
        ("Kopi", "Kopi"),
        ("Minuman", "Minuman"),
        ("Makanan", "Makanan")],
        string="Kategori")

    @api.depends('bahan.harga')
    def _compute_harga(self):
        for produk in self:
            produk.harga = sum(bahan.harga * bahan.stok for bahan in produk.bahan)

class Bahan(models.Model):
    _name = "hmcoffee.produk.bahan"
    _description = "model.technical.name"
    _rec_name="nama"

    nama = fields.Char(string="Nama Bahan")
    harga = fields.Integer(string="Harga")
    stok = fields.Integer(string="Stock Barang")

    bahan_id = fields.Many2one(
        comodel_name='hmcoffee.produk', 
        string="Produk",
        ondelete="cascade")
    supplier_id = fields.Many2many(
        comodel_name='hmcoffee.supplier'
    )
