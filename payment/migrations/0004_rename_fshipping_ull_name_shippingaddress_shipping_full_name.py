# Generated by Django 5.1.2 on 2024-10-20 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_order_orderitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='fshipping_ull_name',
            new_name='shipping_full_name',
        ),
    ]
