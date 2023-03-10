# Generated by Django 4.1.5 on 2023-01-07 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0006_product_quantity_alter_product_description_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="slug",
            field=models.SlugField(default="", max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(default="description"),
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.FloatField(default=0.0),
        ),
    ]
