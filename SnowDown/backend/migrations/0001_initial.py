# Generated by Django 3.2.9 on 2021-11-07 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal', models.CharField(max_length=400, unique=True)),
                ('acronym', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Death',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('options', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='FAST',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('options', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='How_ID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('options', models.CharField(max_length=30)),
                ('acronym', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Incident_Photos_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='Report_Images/')),
            ],
        ),
        migrations.CreateModel(
            name='Island',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('island', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('options', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Observer_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observer_type', models.CharField(max_length=20)),
                ('acronym', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SealSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('options', models.CharField(max_length=30)),
                ('acronym', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observer_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Sex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('options', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('options', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='TagColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('options', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='TagSide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('options', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_type', models.CharField(max_length=100)),
                ('acronym', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TokenIssued',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.TextField()),
                ('email', models.EmailField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='SubAnimal_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subAnimal', models.CharField(max_length=400, unique=True)),
                ('acronym', models.CharField(blank=True, max_length=200)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.animal_table')),
            ],
        ),
        migrations.CreateModel(
            name='Incident_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ticket_Number', models.CharField(max_length=15)),
                ('Hotline_Operator_Initials', models.CharField(blank=True, max_length=4)),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=500)),
                ('Observer_Initials', models.CharField(max_length=4)),
                ('location', models.CharField(max_length=500)),
                ('lat', models.DecimalField(db_index=True, decimal_places=15, max_digits=19)),
                ('lng', models.DecimalField(db_index=True, decimal_places=15, max_digits=19)),
                ('locationDetails', models.TextField(blank=True)),
                ('Animal_Present', models.BooleanField(default=False)),
                ('beach_Position', models.BooleanField(blank=True)),
                ('BleachNumber', models.CharField(blank=True, max_length=10)),
                ('Tag_Number', models.CharField(blank=True, max_length=10)),
                ('ID_Perm', models.CharField(blank=True, max_length=10)),
                ('Molt', models.BooleanField(blank=True)),
                ('ID_Description', models.TextField(blank=True)),
                ('ID_Verified_by', models.CharField(max_length=100)),
                ('SealLogging', models.BooleanField(blank=True)),
                ('MomPup', models.BooleanField(blank=True)),
                ('SRA_Set_Up', models.BooleanField(blank=True)),
                ('SRA_Set_by', models.CharField(blank=True, max_length=100)),
                ('Volunteers_Engaged', models.IntegerField(blank=True)),
                ('Seal_Depart', models.BooleanField(blank=True)),
                ('Seal_Depart_Date', models.DateField(blank=True)),
                ('Seal_Depart_Time', models.TimeField(blank=True)),
                ('description', models.TextField()),
                ('size', models.CharField(blank=True, max_length=10)),
                ('Responder', models.CharField(blank=True, max_length=100)),
                ('Responder_Arrived', models.TimeField(blank=True)),
                ('Responder_Left', models.TimeField(blank=True)),
                ('Outreach_Provided', models.BooleanField()),
                ('Delivered', models.BooleanField(blank=True)),
                ('CauseOfDeath', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='backend.death')),
                ('FAST', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='backend.fast')),
                ('How_ID', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='backend.how_id')),
                ('Observer_Type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.observer_type')),
                ('SealSize', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='backend.sealsize')),
                ('Sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.sector')),
                ('Tag_Color', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='backend.tagcolor')),
                ('Tag_Side', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='backend.tagside')),
                ('Ticket_Type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.ticket_type')),
                ('Where_To', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='backend.location')),
                ('animalType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.subanimal_table')),
                ('onIsland', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='backend.island')),
                ('photos', models.ManyToManyField(to='backend.Incident_Photos_Table')),
                ('sex', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='backend.sex')),
                ('status', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='backend.status')),
            ],
        ),
        migrations.CreateModel(
            name='Group_Incident_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top', models.DecimalField(db_index=True, decimal_places=15, max_digits=19)),
                ('bottom', models.DecimalField(db_index=True, decimal_places=15, max_digits=19)),
                ('left', models.DecimalField(db_index=True, decimal_places=15, max_digits=19)),
                ('right', models.DecimalField(db_index=True, decimal_places=15, max_digits=19)),
                ('Ticket_Number', models.CharField(max_length=15)),
                ('Hotline_Operator_Initials', models.CharField(blank=True, max_length=4)),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=500)),
                ('Observer_Initials', models.CharField(max_length=4)),
                ('location', models.CharField(max_length=500)),
                ('lat', models.DecimalField(db_index=True, decimal_places=15, max_digits=19)),
                ('lng', models.DecimalField(db_index=True, decimal_places=15, max_digits=19)),
                ('locationDetails', models.TextField(blank=True)),
                ('Animal_Present', models.BooleanField(default=False)),
                ('beach_Position', models.BooleanField(blank=True)),
                ('BleachNumber', models.CharField(blank=True, max_length=10)),
                ('Tag_Number', models.CharField(blank=True, max_length=10)),
                ('ID_Perm', models.CharField(blank=True, max_length=10)),
                ('Molt', models.BooleanField(blank=True)),
                ('ID_Description', models.TextField(blank=True)),
                ('ID_Verified_by', models.CharField(max_length=100)),
                ('SealLogging', models.BooleanField(blank=True)),
                ('MomPup', models.BooleanField(blank=True)),
                ('SRA_Set_Up', models.BooleanField(blank=True)),
                ('SRA_Set_by', models.CharField(blank=True, max_length=100)),
                ('Volunteers_Engaged', models.IntegerField(blank=True)),
                ('Seal_Depart', models.BooleanField(blank=True)),
                ('Seal_Depart_Date', models.DateField(blank=True)),
                ('Seal_Depart_Time', models.TimeField(blank=True)),
                ('description', models.TextField()),
                ('size', models.CharField(blank=True, max_length=10)),
                ('Responder', models.CharField(blank=True, max_length=100)),
                ('Responder_Arrived', models.TimeField(blank=True)),
                ('Responder_Left', models.TimeField(blank=True)),
                ('Outreach_Provided', models.BooleanField()),
                ('Delivered', models.BooleanField(blank=True)),
                ('CauseOfDeath', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='backend.death')),
                ('FAST', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='backend.fast')),
                ('How_ID', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='backend.how_id')),
                ('Observer_Type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.observer_type')),
                ('SealSize', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='backend.sealsize')),
                ('Sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.sector')),
                ('Tag_Color', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='backend.tagcolor')),
                ('Tag_Side', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='backend.tagside')),
                ('Ticket_Type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.ticket_type')),
                ('Where_To', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='backend.location')),
                ('animalType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.subanimal_table')),
                ('incident', models.ManyToManyField(to='backend.Incident_Table')),
                ('onIsland', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='backend.island')),
                ('sex', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='backend.sex')),
                ('status', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='backend.status')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=225, unique=True)),
                ('phone', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('Last_name', models.CharField(max_length=255)),
                ('Volunteer', models.BooleanField(default=True)),
                ('Picture', models.ImageField(default='User Profile Pic/default.png', upload_to='User Profile Pic/')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
