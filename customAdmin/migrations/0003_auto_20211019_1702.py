# Generated by Django 3.2.6 on 2021-10-19 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customAdmin', '0002_remove_product_weight_in_kg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='modified_on',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
