# Generated by Django 4.2 on 2023-05-03 04:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_merge_20230502_1108'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-created_at',), 'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
    ]