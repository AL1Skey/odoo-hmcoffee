from odoo import api,models,fields

class Produk(models.Model):
    _name = "hmcoffee.produk"
    _description = "model.technical.name"
    
    pesanan_id = fields.Many2one(comodel_name="hmcoffee.pesanan",string="product_id")
    name = fields.Char(string="Nama Produk")
    bahan_ids = fields.One2many(comodel_name="hmcoffee.produk.bahan",inverse_name="produk_id", string="Bahan")
    harga = fields.Float(readonly=True, string="Harga", compute="_compute_harga")
    kategori = fields.Selection(selection=[
        ("Kopi", "Kopi"),
        ("Minuman", "Minuman"),
        ("Makanan", "Makanan")],
        string="Kategori")

    @api.depends('harga')
    def _compute_harga(self):
        for produk in self:
            produk.harga = sum(bahan.harga * bahan.stok for bahan in produk.bahan)

class Bahan(models.Model):
    _name = "hmcoffee.produk.bahan"
    _description = "model.technical.name"
    _rec_name = "name"

    name = fields.Char(string="Nama Bahan")
    harga = fields.Integer(string="Harga")
    stok = fields.Integer(string="Stock Barang")

    produk_id = fields.Many2one(
        comodel_name='hmcoffee.produk', 
        string="Produk",
        ondelete="cascade")
    supplier_id = fields.Many2many(
        comodel_name='hmcoffee.supplier', string="Supplier"
    )
