# Generated by Django 5.1.2 on 2024-10-20 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0007_alter_orderitem_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='amount_paid',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
    ]
