# Generated by Django 3.2.8 on 2021-10-29 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_alter_animal_characteristics_table_characteristicstag'),
    ]

    operations = [
        migrations.AddField(
            model_name='incident_table',
            name='people',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]