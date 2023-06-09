# Generated by Django 4.2 on 2023-04-30 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_warehouseitem_options'),
        ('orders', '0004_alter_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='warehouse_item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='shop.warehouseitem'),
        ),
    ]
