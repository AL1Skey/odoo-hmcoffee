from odoo import fields,models,api

class Pesanan(models.Model):
    _name="hmcoffee.pesanan"
    _description="model.technical.name"

    pesanan_id = fields.Char(string="Kode Pesanan",readonly=True, default=lambda self:('New'))
    pelanggan=fields.Many2one(comodel_name="hmcoffee.pelanggan",string="Pelanggan")
    produk=fields.One2many(comodel_name="hmcoffee.produk")
    quantity=fields.Integer(string="Quantity")
    harga=fields.Float(string="Harga",digits=2,default=sum([i.harga for i in produk]))
    