# Generated by Django 3.0.2 on 2020-02-23 11:12

from django.conf import settings
import django.core.validators
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
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='user')),
                ('coc_version', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^202[\\d].[\\d]+$', 'Not a valid CoC version')], verbose_name='latest agreed CoC version')),
            ],
        ),
    ]
