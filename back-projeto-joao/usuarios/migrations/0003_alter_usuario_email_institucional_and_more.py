# Generated by Django 5.1.1 on 2024-10-03 00:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('usuarios', '0002_alter_usuario_options_alter_usuario_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='email_institucional',
            field=models.EmailField(max_length=254, unique=True, validators=[django.core.validators.RegexValidator(message='O e-mail deve ser um e-mail institucional (@ufersa.edu.br).', regex='^.+@ufersa\\.edu\\.br$')]),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='usuario_groups', to='auth.group'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='usuario_permissions', to='auth.permission'),
        ),
    ]
