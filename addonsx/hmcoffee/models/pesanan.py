from odoo import fields,models,api

class Pesanan(models.Model):
    _name="hmcoffee.pesanan"
    _description="model.technical.name"

    pesanan_id = fields.Char(string="Kode Pesanan",readonly=True, default=lambda self:('New'))
    pelanggan=fields.Many2one(comodel_name="hmcoffee.pelanggan",string="Pelanggan")
    produk_ids=fields.One2many(comodel_name="hmcoffee.produk",inverse_name="pesanan_id",string="Produk")
    quantity=fields.Integer(string="Quantity")
    harga=fields.Float(string="Harga",digits=2,compute="_total_harga")
    
    @api.depends('harga')
    def _total_harga(self):
        for pesanan in self:
            pesanan.harga=sum(produk.harga for produk in pesanan.produk)
    