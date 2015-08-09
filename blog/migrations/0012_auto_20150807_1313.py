# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_comentario_mail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='mail',
            field=models.TextField(verbose_name='Mail'),
        ),
    ]
