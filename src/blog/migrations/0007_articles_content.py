# Generated by Django 4.2 on 2023-06-01 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_articles_options_alter_articles_img_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='content',
            field=models.TextField(default='hello'),
            preserve_default=False,
        ),
    ]
