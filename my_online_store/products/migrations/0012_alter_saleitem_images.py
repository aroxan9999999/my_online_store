# Generated by Django 4.2.4 on 2023-09-02 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_alter_image_src'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saleitem',
            name='images',
            field=models.ManyToManyField(to='products.image'),
        ),
    ]
