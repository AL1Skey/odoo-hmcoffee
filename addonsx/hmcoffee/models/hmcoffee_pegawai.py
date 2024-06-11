from odoo import models, fields, api

class Pegawai(models.Model):
    _name="hmcoffee.pegawai"
    _description="model.technical.name"

    nama = fields.Char(string='Nama')
    usia = fields.Integer(string="Usia")

