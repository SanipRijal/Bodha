# Generated by Django 2.2.3 on 2019-08-10 16:13

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_bannerimage_cropping'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventimage',
            name='listing',
            field=image_cropping.fields.ImageRatioField('image', '520x292', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='listing'),
        ),
    ]
