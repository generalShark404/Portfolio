# Generated by Django 5.0.6 on 2024-07-11 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app_1', '0010_remove_project_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectfeature',
            name='header',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
