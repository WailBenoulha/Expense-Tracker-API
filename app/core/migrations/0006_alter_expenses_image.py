# Generated by Django 5.1.3 on 2024-12-08 19:46

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_expenses_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=core.models.image_file_path),
        ),
    ]
