# Generated by Django 3.2.2 on 2021-05-09 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_gallery1_gallery2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gallery1',
            old_name='category',
            new_name='name',
        ),
    ]
