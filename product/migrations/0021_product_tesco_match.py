# Generated by Django 3.2.10 on 2022-04-19 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0020_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tesco_match',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
