# Generated by Django 3.2.2 on 2021-05-19 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_alter_order_resprepstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='comment',
            field=models.CharField(default='', max_length=255),
        ),
    ]
