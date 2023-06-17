# Generated by Django 4.2 on 2023-06-17 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameapp', '0005_alter_game_datum_alter_game_icon_alter_game_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='zanr',
        ),
        migrations.RemoveField(
            model_name='game',
            name='hodnoceni',
        ),
        migrations.AddField(
            model_name='game',
            name='hodnoceni',
            field=models.CharField(choices=[('1', 'VERY BAD'), ('2', 'BAD'), ('3', 'AVERAGE'), ('4', 'GOOD'), ('5', 'VERY GOOD')], default='1', help_text='Zadej hodnocení', max_length=1, verbose_name='Hodnocení'),
        ),
    ]
