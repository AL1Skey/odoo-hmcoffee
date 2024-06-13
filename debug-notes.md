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
- view tidak tampil dikarenakan akses kontrol. biasanya di Id, Id itu tidak boleh duplikat di csv security
> sebelum
```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_hmcoffee_pegawai,hmcoffee.pegawai,model_hmcoffee_pegawai,,1,1,1,1
access_hmcoffee_produk,access_hmcoffee_produk,model_hmcoffee_produk,,1,1,1,1
access_hmcoffee_produk,hmcoffee.produk.bahan,model_hmcoffee_produk_bahan,,1,1,1,1
access_hmcoffee_pesanan,hmcoffee.pesanan,model_hmcoffee_pesanan,,1,1,1,1
```
> sesudah
```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_hmcoffee_pegawai,hmcoffee.pegawai,model_hmcoffee_pegawai,,1,1,1,1
access_hmcoffee_produk,access_hmcoffee_produk,model_hmcoffee_produk,,1,1,1,1
access_hmcoffee_produk_bahan,hmcoffee.produk.bahan,model_hmcoffee_produk_bahan,,1,1,1,1
access_hmcoffee_pesanan,hmcoffee.pesanan,model_hmcoffee_pesanan,,1,1,1,1
```

- Jika ada error di view:
    - jika ada error di view dan muncul di terminal, maka errornya ada di ketidakcocokan antara nama fields di view dan nama fields di model
    - jika tidak ada error di terminal, maka errornya mungkin terdapat di security yang mana sepertinya ada yang duplikat

- Cara debug error 'odoo.exceptions.UserError: No inverse field None found for 'your-model-name'':
> komenin semua model yang ada di init
```py
# # -*- coding: utf-8 -*-

# from . import models
# from . import hmcoffee_pegawai
# # from . import pesanan
# from . import produk
# from . import supplier
# # from . import pembelian
```
> buka komen satu per satu lalu rerun sampai muncul error tersebut
```py
# # -*- coding: utf-8 -*-

from . import models
# from . import hmcoffee_pegawai
# # from . import pesanan
# from . import produk
# from . import supplier
# # from . import pembelian
```
```py
# # -*- coding: utf-8 -*-

from . import models
from . import hmcoffee_pegawai
# # from . import pesanan
# from . import produk
# from . import supplier
# # from . import pembelian
```
```py
# # -*- coding: utf-8 -*-

from . import models
from . import hmcoffee_pegawai
from . import pesanan
# from . import produk
# from . import supplier
# # from . import pembelian
```
> Setelah ketemu model yang bermasalah, debug model tsb. Biasanya error seperti ini karena inverse_fieldnya tidak sesuai satu sama lainnya atau belum dimasukin inverse_fieldnya di one2many.

- Yang di