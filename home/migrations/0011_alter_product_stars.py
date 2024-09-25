# Generated by Django 5.0.6 on 2024-09-20 20:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_product_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stars',
            field=models.IntegerField(default=1, max_length=255, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]