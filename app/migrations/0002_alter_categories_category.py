# Generated by Django 4.2.4 on 2023-09-03 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='category',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
