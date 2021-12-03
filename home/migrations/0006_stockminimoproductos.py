# Generated by Django 3.2.3 on 2021-11-04 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_ventas_cod_art'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockMinimoProductos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_art', models.CharField(blank=True, max_length=100, null=True)),
                ('stock_mat', models.IntegerField(blank=True, null=True)),
                ('stock_bul', models.IntegerField(blank=True, null=True)),
                ('stock_bod', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
