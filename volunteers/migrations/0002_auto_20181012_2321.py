# Generated by Django 2.1.1 on 2018-10-12 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='contact_number',
            field=models.IntegerField(),
        ),
    ]