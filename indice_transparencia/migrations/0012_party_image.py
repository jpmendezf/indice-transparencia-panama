# Generated by Django 2.1.4 on 2019-01-18 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indice_transparencia', '0011_auto_20190117_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='party_logos/%Y/%m/%d/', verbose_name='Logo del partido'),
        ),
    ]
