# Generated by Django 4.1.1 on 2022-10-03 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='delivery_address',
            field=models.CharField(max_length=127),
        ),
        migrations.AlterField(
            model_name='cart',
            name='total_price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cart',
            name='user_name',
            field=models.CharField(max_length=127),
        ),
        migrations.AlterField(
            model_name='cartproduct',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_products', to='mainapp.cart'),
        ),
        migrations.AlterField(
            model_name='cartproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_products', to='mainapp.product'),
        ),
    ]
