# Generated by Django 3.1.4 on 2021-01-06 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('historias', '0002_medico_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medico',
            old_name='user',
            new_name='usuario',
        ),
    ]