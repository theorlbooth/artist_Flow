# Generated by Django 3.0.2 on 2020-01-10 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0004_auto_20200110_1019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='lastFMId',
            new_name='deezerId',
        ),
    ]
