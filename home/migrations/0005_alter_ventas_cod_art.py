# Generated by Django 3.2.3 on 2021-11-02 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_ventas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ventas',
            name='cod_art',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
