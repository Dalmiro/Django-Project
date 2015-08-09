# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_contacto_celu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('autor', models.CharField(max_length=100, verbose_name='Nombre')),
                ('mensaje', models.TextField(verbose_name='Mensaje')),
                ('post', models.ForeignKey(to='blog.Entrada')),
            ],
        ),
    ]
