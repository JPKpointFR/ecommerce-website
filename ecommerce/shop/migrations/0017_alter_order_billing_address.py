# Generated by Django 4.1.3 on 2023-01-17 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0016_alter_order_billing_address_alter_order_country_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="billing_address",
            field=models.CharField(max_length=201),
        ),
    ]