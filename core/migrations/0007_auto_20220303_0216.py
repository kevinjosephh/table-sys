# Generated by Django 3.2.6 on 2022-03-03 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_table_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='time',
            field=models.DateTimeField(blank=True),
        ),
        migrations.DeleteModel(
            name='Reservation',
        ),
    ]
