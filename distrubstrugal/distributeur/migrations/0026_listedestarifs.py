# Generated by Django 3.2 on 2022-02-15 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distributeur', '0025_remove_commande_totalettc'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListeDesTarifs',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]