# Generated by Django 3.2 on 2021-05-18 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distributeur', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='prix_unitaire',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='commande',
            name='date',
            field=models.CharField(default='18/05/2021', max_length=255),
        ),
    ]
