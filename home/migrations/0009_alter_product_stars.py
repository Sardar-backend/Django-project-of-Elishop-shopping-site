# Generated by Django 5.0.6 on 2024-09-20 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_product_warranty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stars',
            field=models.CharField(default='*', max_length=255),
        ),
    ]
