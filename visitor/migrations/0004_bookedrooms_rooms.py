# Generated by Django 3.1.2 on 2020-11-18 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0003_auto_20201103_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookedrooms',
            name='rooms',
            field=models.CharField(default=0, max_length=20),
        ),
    ]
