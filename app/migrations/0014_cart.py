# Generated by Django 3.2.5 on 2021-07-15 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20210715_1142'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('cart_price', models.BigIntegerField(default=0)),
                ('cart_quantity', models.BigIntegerField(default=1)),
                ('cart_date', models.DateTimeField(auto_now_add=True)),
                ('cart_subtotal', models.BigIntegerField(default=0)),
                ('tax', models.BigIntegerField(default=18)),
                ('cart_total', models.BigIntegerField(default=0)),
                ('order_status', models.CharField(default='Order Confirmation Pending', max_length=50)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.products')),
                ('profile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profile')),
            ],
        ),
    ]
