# Generated by Django 3.2.5 on 2021-07-15 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20210715_1016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='address',
        ),
        migrations.AddField(
            model_name='profile',
            name='address_line1',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='address_line2',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='state',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='zipcode',
            field=models.BigIntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='ShippingAddress',
        ),
    ]