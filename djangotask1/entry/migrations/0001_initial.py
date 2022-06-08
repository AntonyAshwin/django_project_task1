# Generated by Django 4.0.4 on 2022-06-07 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=32)),
                ('lname', models.CharField(max_length=32)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='')),
                ('role', models.CharField(choices=[('DOCTOR', 'DOCTOR'), ('PATIENT', 'PATIENT')], default='PATIENT', max_length=32)),
                ('username', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('confirm_password', models.CharField(max_length=50)),
                ('econtact', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'signupform',
            },
        ),
    ]
