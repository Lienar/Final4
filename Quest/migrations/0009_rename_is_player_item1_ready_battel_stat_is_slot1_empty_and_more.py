# Generated by Django 5.1.1 on 2024-10-16 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quest', '0008_location_trap_trap_exists'),
    ]

    operations = [
        migrations.RenameField(
            model_name='battel_stat',
            old_name='Is_player_item1_ready',
            new_name='Is_slot1_empty',
        ),
        migrations.RenameField(
            model_name='battel_stat',
            old_name='Is_player_item2_ready',
            new_name='Is_slot2_empty',
        ),
        migrations.RenameField(
            model_name='battel_stat',
            old_name='Is_player_item3_ready',
            new_name='Is_slot3_empty',
        ),
        migrations.RenameField(
            model_name='battel_stat',
            old_name='Is_player_item4_ready',
            new_name='Is_slot4_empty',
        ),
        migrations.RenameField(
            model_name='battel_stat',
            old_name='Is_player_item5_ready',
            new_name='Is_slot5_empty',
        ),
        migrations.RenameField(
            model_name='battel_stat',
            old_name='Is_player_item6_ready',
            new_name='Is_slot6_empty',
        ),
    ]