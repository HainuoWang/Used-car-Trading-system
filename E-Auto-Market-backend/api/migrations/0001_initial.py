# Generated by Django 3.1.5 on 2021-04-12 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TempUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=200)),
                ('token', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=200)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('create_date', models.DateField(blank=True, null=True, verbose_name='create date')),
                ('balance', models.FloatField(blank=True, null=True)),
                ('roles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='api.role')),
            ],
        ),
    ]