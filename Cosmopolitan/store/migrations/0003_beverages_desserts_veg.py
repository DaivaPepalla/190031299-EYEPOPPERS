# Generated by Django 3.2.2 on 2021-05-08 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_nonveg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Veg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('image', models.ImageField(upload_to='images/')),
                ('slug', models.SlugField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('time', models.CharField(max_length=255)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vegitem', to='store.menu')),
            ],
            options={
                'verbose_name_plural': 'veg',
            },
        ),
        migrations.CreateModel(
            name='Desserts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('image', models.ImageField(upload_to='images/')),
                ('slug', models.SlugField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('time', models.CharField(max_length=255)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dessertitem', to='store.menu')),
            ],
            options={
                'verbose_name_plural': 'desserts',
            },
        ),
        migrations.CreateModel(
            name='Beverages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('image', models.ImageField(upload_to='images/')),
                ('slug', models.SlugField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('time', models.CharField(max_length=255)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beverageitem', to='store.menu')),
            ],
            options={
                'verbose_name_plural': 'beverages',
            },
        ),
    ]
