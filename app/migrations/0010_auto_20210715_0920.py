# Generated by Django 3.2.5 on 2021-07-15 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_profile_shippingaddress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='zipcode',
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='zipcode',
            field=models.BigIntegerField(null=True),
        ),
    ]