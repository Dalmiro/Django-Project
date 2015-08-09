# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20150807_0048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mensajes',
            name='published_in',
        ),
        migrations.DeleteModel(
            name='Mensajes',
        ),
    ]
