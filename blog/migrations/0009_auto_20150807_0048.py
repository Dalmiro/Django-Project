# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20150807_0045'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contacto',
            options={'ordering': ['-fecha'], 'verbose_name': 'Contacto', 'verbose_name_plural': 'Contactos'},
        ),
        migrations.AlterModelOptions(
            name='entrada',
            options={'ordering': ['-fecha'], 'verbose_name': 'Mi Entrada', 'verbose_name_plural': 'Mis entradas'},
        ),
        migrations.AlterModelOptions(
            name='mensajes',
            options={'ordering': ['-fecha'], 'verbose_name': 'Mensaje', 'verbose_name_plural': 'Comentarios'},
        ),
    ]
