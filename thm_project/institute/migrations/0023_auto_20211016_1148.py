# Generated by Django 3.1 on 2021-10-16 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0022_plmeasurement'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='plmeasurement',
            options={'default_permissions': (), 'get_latest_by': 'timestamp', 'ordering': ['timestamp'], 'verbose_name': 'PL measurement', 'verbose_name_plural': 'PL measurements'},
        ),
    ]