# Generated by Django 3.1 on 2021-10-18 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0029_auto_20211018_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thicknessmeasurement',
            name='thickness',
            field=models.DecimalField(decimal_places=2, help_text='bla / cm<sup>3</sup>', max_digits=7, verbose_name='thicknes'),
        ),
    ]
