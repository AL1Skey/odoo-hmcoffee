from odoo import models, fields, api
import datetime
class Pegawai(models.Model):
    _name="hmcoffee.pegawai"
    _description="model.technical.name"

    nama = fields.Char(string='Nama')
    usia = fields.Integer(string="Usia")
    jabatan = fields.Selection(selection=[
        ("Barista","Barista"),
        ("Staff","Staff"),
        ("Manager","Manager")],
        string="Jabatan")
    gaji = fields.Float(string="Gaji")
    masuk = fields.Datetime(string="Bekerja Sejak")
    keluar = fields.Datetime(string="Keluar Sejak")
    

