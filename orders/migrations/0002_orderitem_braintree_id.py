# Generated by Django 4.0 on 2022-01-06 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='braintree_id',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
