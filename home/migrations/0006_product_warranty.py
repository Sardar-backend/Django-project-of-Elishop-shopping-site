# Generated by Django 5.0.6 on 2024-09-20 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_product_favorites_customuser_favorites'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='warranty',
            field=models.CharField(choices=[('no_warranty', 'بدون گارانتی'), ('six_months', 'شش ماهه'), ('one_year', 'یک ساله')], default='no_warranty', max_length=20),
        ),
    ]
