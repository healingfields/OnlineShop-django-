# Generated by Django 4.0 on 2022-01-07 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_orderitem_braintree_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='braintree_id',
        ),
        migrations.AddField(
            model_name='order',
            name='braintree_id',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
