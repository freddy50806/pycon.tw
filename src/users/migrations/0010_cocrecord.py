# Generated by Django 3.0.2 on 2020-02-23 12:28

import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20160227_1656'),
    ]

    operations = [
        migrations.CreateModel(
            name='CocRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coc_version', models.CharField(max_length=15, verbose_name='latest agreed CoC version')),
                ('user', core.models.BigForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
    ]
