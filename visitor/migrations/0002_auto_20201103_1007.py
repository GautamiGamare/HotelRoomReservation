# Generated by Django 3.1.2 on 2020-11-03 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookedrooms',
            old_name='type',
            new_name='roomId',
        ),
    ]
