# Generated by Django 4.2.4 on 2023-09-03 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('image', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.ImageField(upload_to='images/')),
                ('alt', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField()),
                ('rate', models.PositiveSmallIntegerField()),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SaleItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('salePrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dateFrom', models.DateField()),
                ('dateTo', models.DateField()),
                ('images', models.ManyToManyField(to='products.image')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('count', models.PositiveIntegerField(default=1)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True)),
                ('fullDescription', models.TextField(blank=True)),
                ('freeDelivery', models.BooleanField(default=True)),
                ('rating', models.DecimalField(decimal_places=2, default=4.6, max_digits=3)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
                ('images', models.ManyToManyField(blank=True, related_name='products', to='products.image')),
                ('reviews', models.ManyToManyField(related_name='products', to='products.review')),
                ('specifications', models.ManyToManyField(related_name='products', to='products.specification')),
                ('tags', models.ManyToManyField(related_name='products', to='products.tag')),
            ],
            options={
                'db_table': 'product_full',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='subcategories',
            field=models.ManyToManyField(to='products.subcategory'),
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='banners/')),
                ('text', models.CharField(max_length=255)),
                ('link', models.URLField()),
                ('products', models.ManyToManyField(to='products.product')),
            ],
        ),
    ]
