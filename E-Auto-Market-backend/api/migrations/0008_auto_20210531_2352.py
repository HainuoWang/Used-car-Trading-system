# Generated by Django 3.1.5 on 2021-05-31 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_order_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
