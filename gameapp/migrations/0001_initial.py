# Generated by Django 4.2 on 2023-05-12 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a name of Developer', max_length=50, unique=True, verbose_name='Developer name')),
                ('popis', models.TextField(blank=True, help_text='Enter description of their work', null=True)),
            ],
            options={
                'verbose_name': 'Vývojář',
                'verbose_name_plural': 'Vývojáři',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Firma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a name of Company', max_length=50, unique=True, verbose_name='Company name')),
                ('Sidlo', models.CharField(blank=True, help_text='Enter Company address', max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Firma',
                'verbose_name_plural': 'Firmy',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Žánr',
                'verbose_name_plural': 'Žánry',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Hodnoceni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Hodnoceni',
                'verbose_name_plural': 'Hodnoceni',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a name of Game', max_length=50, unique=True, verbose_name='Game name')),
                ('popis', models.TextField(blank=True, help_text='Enter description of the game', null=True)),
                ('datum', models.DateField(blank=True, null=True, verbose_name='datum vydání')),
                ('hodnoceni', models.ManyToManyField(to='gameapp.hodnoceni')),
                ('zanr', models.ManyToManyField(to='gameapp.genres')),
            ],
            options={
                'verbose_name': 'Hra',
                'verbose_name_plural': 'hry',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Costumer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a name of Costumer', max_length=50, unique=True, verbose_name='Costumer name')),
                ('profilovka', models.ImageField(upload_to='company', verbose_name='Fotografie')),
                ('email', models.CharField(default='it2001@sspu-opava.cz', help_text='email', max_length=50, unique=True, verbose_name='Costumer email')),
                ('datum', models.DateField(auto_now_add=True)),
                ('hry', models.ManyToManyField(to='gameapp.game')),
            ],
            options={
                'verbose_name': 'Zakazník',
                'verbose_name_plural': 'Zakazníci',
                'ordering': ['-name'],
            },
        ),
    ]
