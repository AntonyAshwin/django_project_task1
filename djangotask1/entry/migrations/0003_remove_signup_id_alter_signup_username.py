# Generated by Django 4.0.4 on 2022-06-07 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0002_remove_signup_econtact_signup_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='id',
        ),
        migrations.AlterField(
            model_name='signup',
            name='username',
            field=models.CharField(max_length=32, primary_key=True, serialize=False),
        ),
    ]
