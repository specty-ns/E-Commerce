# Generated by Django 3.2.5 on 2021-07-14 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='product_brand',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='products',
            name='product_category',
            field=models.CharField(default='', max_length=50),
        ),
    ]
