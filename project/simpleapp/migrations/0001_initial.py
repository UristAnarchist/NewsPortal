# Generated by Django 4.2.3 on 2023-07-10 17:06

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('text', models.TextField()),
                ('amount_of_pages', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('date', models.DateTimeField(default=datetime.datetime(2023, 7, 11, 2, 6, 26, 951863))),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='simpleapp.category')),
            ],
        ),
    ]