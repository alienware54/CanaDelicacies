# Generated by Django 4.2 on 2024-12-03 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('canaapp', '0004_rename_reservations_reservation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='requests',
            new_name='message',
        ),
    ]
