# Generated by Django 2.0.1 on 2020-10-26 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RoomModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('type', models.CharField(choices=[('Standard', 'Standard'), ('Deluxe', 'Deluxe'), ('Luxury', 'Luxury'), ('Sea facing', 'Sea facing')], max_length=20)),
                ('beds', models.IntegerField()),
                ('capacity', models.IntegerField()),
            ],
        ),
    ]
