# Generated by Django 4.0.5 on 2022-06-19 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='image',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
