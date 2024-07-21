# Generated by Django 5.0.6 on 2024-07-10 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app_1', '0008_person_facebook_person_instagram_person_linkedin_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('status', 'Live'), ('status', 'Not Hosted')], max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.CharField(max_length=150, null=True),
        ),
    ]