# Generated by Django 4.2.4 on 2023-09-06 16:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0005_categoryimage_alter_subcategory_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=16)),
                ('name', models.CharField(max_length=255)),
                ('month', models.CharField(max_length=2)),
                ('year', models.CharField(max_length=4)),
                ('code', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.product')),
            ],
            bases=('products.product',),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('fullName', models.CharField(blank=True, max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('deliveryType', models.CharField(blank=True, max_length=255, null=True)),
                ('paymentType', models.CharField(blank=True, max_length=255, null=True)),
                ('totalCost', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('status', models.CharField(blank=True, choices=[('active', 'Active'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='active', max_length=25)),
                ('city', models.CharField(blank=True, max_length=255)),
                ('address', models.TextField(blank=True)),
                ('products', models.ManyToManyField(to='order.productorder')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
