# Generated by Django 3.2.5 on 2021-07-14 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_products_wear_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='wear_by',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Unisex', 'Unisex')], default='Unisex', max_length=10),
        ),
    ]
