# Generated by Django 3.0.1 on 2020-01-24 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(max_length=50, null=True),
        ),
    ]
