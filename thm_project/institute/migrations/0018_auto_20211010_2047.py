# Generated by Django 3.1 on 2021-10-10 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0017_auto_20211010_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thicknessmeasurement',
            name='thickness',
            field=models.DecimalField(decimal_places=2, help_text='*', max_digits=7, verbose_name='thicknes'),
        ),
    ]