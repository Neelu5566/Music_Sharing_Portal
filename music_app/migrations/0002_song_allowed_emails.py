# Generated by Django 4.2.1 on 2023-06-16 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='allowed_emails',
            field=models.TextField(blank=True, null=True),
        ),
    ]
