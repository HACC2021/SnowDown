# Generated by Django 3.2.8 on 2021-10-29 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_alter_tokenissued_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal_table',
            name='animal',
            field=models.CharField(max_length=400, unique=True),
        ),
        migrations.AlterField(
            model_name='subanimal_table',
            name='subAnimal',
            field=models.CharField(max_length=400, unique=True),
        ),
    ]