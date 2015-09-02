# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_newscategory_key_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newscategory',
            name='key_image',
            field=filer.fields.image.FilerImageField(related_name='category_key_image', default=1, to=b'filer.Image', help_text='Optional. Please supply an image, if one is desired. This will be resized automatically.'),
            preserve_default=False,
        ),
    ]
