# Generated by Django 4.2.4 on 2023-09-02 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_images_imageurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='imageUrl',
            field=models.URLField(),
        ),
    ]
