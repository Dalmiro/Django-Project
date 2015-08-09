# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_comentario'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contacto',
            options={'ordering': ['-fecha'], 'verbose_name': 'Contacto', 'verbose_name_plural': 'Todos los contactos'},
        ),
        migrations.AlterModelOptions(
            name='mensajes',
            options={'ordering': ['-fecha'], 'verbose_name': 'Mensaje', 'verbose_name_plural': 'Todos los comentarios'},
        ),
    ]
