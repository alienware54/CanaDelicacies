# Generated by Django 4.2 on 2024-12-03 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('canaapp', '0003_reservations_delete_menuitem'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reservations',
            new_name='Reservation',
        ),
    ]