# Generated by Django 5.1.1 on 2024-10-17 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quest', '0010_battel_stat_player_item1_default_cooldown_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Location_type_empty',
            new_name='Location_empty',
        ),
        migrations.RenameModel(
            old_name='Location_type_enemy',
            new_name='Location_enemy',
        ),
        migrations.RenameModel(
            old_name='Location_type_riddle',
            new_name='Location_riddle',
        ),
    ]