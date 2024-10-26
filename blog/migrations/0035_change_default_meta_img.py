# Generated by Django 4.2.3 on 2023-08-30 06:10

from django.db import migrations
import django_resized.forms
import blog.models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0034_add_default_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="metaimg",
            field=django_resized.forms.ResizedImageField(
                crop=None,
                default=blog.models.get_default_metaimg,
                force_format="WEBP",
                keep_meta=True,
                quality=75,
                scale=None,
                size=[1920, 1080],
                upload_to="post_metaimgs/",
            ),
        ),
    ]
