from odoo import fields,models,api

class Bahan(models.Model):
    _name="hmcoffee.bahan"
    _description="model.technical.name"

    nama=fields.Char(string="Nama Bahan")
    harga=fields.Integer(string="Harga")
    stok=fields.Integer(string="Stock Barang")
    bahan_id=fields.Many2one(comodel_name='hmcoffee.produk',string="bahan_id",readonly=True,default=lambda self:('New'))

class Produk(models.Model):
    _name="hmcoffee.produk"
    _description="model.technical.name"
    
    nama=fields.Char(string="Nama Produk")
    bahan=fields.One2many(comodel_name="hmcoffee.bahan",inverse_name="bahan_id",string="Bahan")
    harga=fields.Float(default=sum([i.harga for i in bahan]), readonly=True, string="Harga")
    kategori=fields.Selection(selection=[
        ("Kopi","Kopi"),
        ("Minuman","Minuman"),
        ("Makanan","Makanan")],
        string="Kategori")
    
