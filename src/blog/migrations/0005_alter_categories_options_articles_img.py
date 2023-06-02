# Generated by Django 4.2 on 2023-06-01 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_articles_auteur_delete_auteurs'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name': 'Catégorie', 'verbose_name_plural': 'Les Catégories'},
        ),
        migrations.AddField(
            model_name='articles',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='articles_pictures/'),
        ),
    ]
