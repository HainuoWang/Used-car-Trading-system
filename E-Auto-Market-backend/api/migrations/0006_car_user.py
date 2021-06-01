# Generated by Django 3.1.5 on 2021-04-13 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210413_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='car_user', to='api.user'),
            preserve_default=False,
        ),
    ]