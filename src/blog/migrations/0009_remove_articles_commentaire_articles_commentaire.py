# Generated by Django 4.2 on 2023-06-01 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_articles_auteur'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='commentaire',
        ),
        migrations.AddField(
            model_name='articles',
            name='commentaire',
            field=models.ManyToManyField(null=True, to='blog.commentaires'),
        ),
    ]
