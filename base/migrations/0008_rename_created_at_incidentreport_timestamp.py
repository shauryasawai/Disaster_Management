# Generated by Django 5.0.7 on 2024-10-13 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_rename_incident_incidentreport'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incidentreport',
            old_name='created_at',
            new_name='timestamp',
        ),
    ]
