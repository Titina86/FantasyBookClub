# Generated by Django 5.0.4 on 2024-11-21 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_adminbook_cover_alter_mybook_cover'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mybook',
            old_name='user',
            new_name='profile',
        ),
    ]