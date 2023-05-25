# Generated by Django 4.2.1 on 2023-05-25 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_clients_alter_projects_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mysite.clients'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='profil',
            field=models.CharField(choices=[('entreprise', 'Entreprise'), ('particulier', 'Particulier')], max_length=50, verbose_name='Status du client'),
        ),
    ]