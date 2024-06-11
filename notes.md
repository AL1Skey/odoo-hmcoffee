klo error pas pip install -r requirements.txt

OS ku: Ubuntu Focal Fossa 20.04
Python-ku: 3.10.4

[Klo mw ganti python default ke 3.10](https://gist.github.com/rutcreate/c0041e842f858ceb455b748809763ddb)

Setelah bikin virtual environment

- jalanin virtual environmentnya

- install wheel
```cmd
pip install wheel
```
- Install package ini sebelum jalanin pip install -r requirements.txt (fix error saat lagi building psycopg2 pillow sama python-ldap)
```bash
sudo apt-get install libpq-dev
sudo apt-get install zlib1g-dev
sudo apt-get install libjpeg8-dev zlib1g-dev libtiff-dev libfreetype6 libfreetype6-dev libwebp-dev libopenjp2-7-dev libimagequant-dev libxcb1-dev libpng-dev
sudo apt-get install libsasl2-dev python-dev libldap2-dev libssl-dev
```

- selalu jalankan ini setiap ada error role="nama" not found
```bash
 sudo -u postgres createuser -s $USER

 createdb $USER
```

- Bikin module MVC di odoo
```bash
./odoo-bin scaffold $nama_module_yg_pengen_dibikin $lokasinya_maunya_dimana
```

- Buat securitynya dengan menyesuaikan nama kelas di model

#### Cth:
> ir.model.access.csv
```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_hmcoffee_pegawai,hmcoffee.pegawai,model_hmcoffee_pegawai,,1,1,1,1
```
> model/hmcoffee_pegawai.py
```py
from odoo import models, fields, api

class Pegawai(models.Model):
    _name="model.technical.name"
    _description="model.technical.name"

    name = fields.Char(string='Nama')
```
- Terus buka security di file \_\_manifest\_\_.py di bagian data
> \_\_manifest\_\_.py
```py
# always loaded
    'data': [
        'security/ir.model.access.csv',#dibagian ini di un-comment
        'views/views.xml',
        'views/templates.xml',
    ],
```