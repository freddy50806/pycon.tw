# Generated by Django 3.0.3 on 2020-03-18 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0022_auto_20200317_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsoredevent',
            name='remoting_policy',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, verbose_name='remoting policy'),
        ),
    ]
