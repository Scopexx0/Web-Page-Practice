# Generated by Django 4.0.4 on 2022-06-09 02:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avatar',
            old_name='imgage',
            new_name='image',
        ),
    ]
