# Generated by Django 5.1.2 on 2024-11-08 14:32

import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0043_update_simularities_on_existing_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='metaimg',
            field=django_resized.forms.ResizedImageField(crop=None, default='default.webp', force_format='WEBP', keep_meta=True, quality=75, scale=None, size=[1920, 1080], upload_to='post_metaimgs'),
        ),
    ]
