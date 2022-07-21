# Generated by Django 3.2.6 on 2021-10-21 19:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customAdmin', '0009_banners'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='customadmin_category_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='coupons',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='coupons',
            name='uses_per_coupons',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='coupons',
            name='uses_per_customer',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='email_template',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='email_template',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customAdmin.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='out_of_stock_status',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='shipping_required',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='product_attribute_association',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customAdmin.product'),
        ),
    ]
