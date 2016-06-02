# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-05-06 07:43
from __future__ import unicode_literals

import core.models
from django.db import migrations, models
import django.db.models.deletion


def add_proposed_talk_events(apps, schema_editor):
    ProposedTalkEvent = apps.get_model('events', 'ProposedTalkEvent')
    TalkProposal = apps.get_model('proposals', 'TalkProposal')
    db_alias = schema_editor.connection.alias

    accepted = TalkProposal.objects.using(db_alias).filter(accepted=True)
    events = [ProposedTalkEvent(proposal=proposal) for proposal in accepted]
    ProposedTalkEvent.objects.using(db_alias).bulk_create(events)


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0027_auto_20160426_1137'),
        ('events', '0004_add_keynoteevent'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProposedTalkEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, choices=[('2-all', 'All rooms'), ('3-r012', 'R0, R1, R2'), ('4-r0', 'R0'), ('5-r1', 'R1'), ('6-r2', 'R2'), ('1-r3', 'R3')], db_index=True, max_length=6, null=True, verbose_name='location')),
            ],
            options={
                'verbose_name_plural': 'talk events',
                'verbose_name': 'talk event',
            },
        ),
        migrations.AddField(
            model_name='proposedtalkevent',
            name='begin_time',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='begined_proposedtalkevent_set', to='events.Time', verbose_name='begin time'),
        ),
        migrations.AddField(
            model_name='proposedtalkevent',
            name='end_time',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ended_proposedtalkevent_set', to='events.Time', verbose_name='end time'),
        ),
        migrations.AddField(
            model_name='proposedtalkevent',
            name='proposal',
            field=core.models.BigForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proposals.TalkProposal', verbose_name='proposal'),
        ),

        migrations.RunPython(
            code=add_proposed_talk_events,
            reverse_code=migrations.RunPython.noop,
        ),
    ]