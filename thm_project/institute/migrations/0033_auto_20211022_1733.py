# Generated by Django 3.1 on 2021-10-22 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0032_auto_20211018_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='substrate',
            name='material',
            field=models.CharField(choices=[('custom', 'custom'), ('si', 'silicon'), ('si-wafer', 'silicon wafer'), ('sic', 'silicon carbide'), ('sapphire', 'sapphire'), ('gan', 'gallium nitride')], max_length=30, verbose_name='substrate material'),
        ),
    ]
