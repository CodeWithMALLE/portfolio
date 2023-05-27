# Generated by Django 4.2.1 on 2023-05-26 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_projects_client_alter_clients_profil'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Prénom')),
                ('last_name', models.CharField(max_length=50, verbose_name='Nom de famille')),
                ('email', models.EmailField(max_length=254, verbose_name='Adresse mail')),
                ('tel', models.CharField(max_length=50, verbose_name='Numéro de téléphone')),
                ('msg', models.TextField()),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Les Contacts',
            },
        ),
    ]