# Generated by Django 3.2 on 2021-08-11 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('distributeur', '0024_alter_article_prix_unitaire'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commande',
            name='totaleTTC',
        ),
    ]