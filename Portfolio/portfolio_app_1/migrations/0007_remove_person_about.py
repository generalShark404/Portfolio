# Generated by Django 5.0.6 on 2024-07-09 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app_1', '0006_alter_person_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='about',
        ),
    ]
