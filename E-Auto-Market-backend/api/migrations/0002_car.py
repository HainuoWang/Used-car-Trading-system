# Generated by Django 3.1.5 on 2021-04-13 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.CharField(max_length=100)),
                ('sub_pictures', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('mileage', models.IntegerField(blank=True, null=True)),
                ('displacement', models.CharField(max_length=20)),
                ('amt', models.CharField(max_length=20)),
            ],
        ),
    ]