# Generated by Django 3.1 on 2021-07-28 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0009_auto_20200901_1457'),
        ('institute', '0004_sorted_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThicknessMeasurement',
            fields=[
                ('process_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='samples.process')),
                ('thickness', models.DecimalField(decimal_places=2, help_text='in nm', max_digits=7, verbose_name='thicknes')),
                ('method', models.CharField(choices=[('profile', 'profile'), ('laser', 'laser'), ('calculated', 'calculated from deposition'), ('estimate', 'estimate'), ('other', 'other')], default='profile', max_length=30, verbose_name='method')),
            ],
            options={
                'ordering': ['timestamp'],
                'get_latest_by': 'timestamp',
                'abstract': False,
                'default_permissions': (),
            },
            bases=('samples.process',),
        ),
    ]
