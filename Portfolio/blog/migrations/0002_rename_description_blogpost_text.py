# Generated by Django 5.0.6 on 2024-07-09 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='description',
            new_name='text',
        ),
    ]