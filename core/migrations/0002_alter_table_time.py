# Generated by Django 3.2.6 on 2022-03-02 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]