# Generated by Django 3.2 on 2022-03-14 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distributeur', '0035_auto_20220305_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='id_154_prixparlist',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='id_154_surcharge',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='id_346_prixparlist',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='id_346_surcharge',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='id_347_prixparlist',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='id_347_surcharge',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='id_376_prixparlist',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='id_376_surcharge',
            field=models.FloatField(default=0),
        ),
    ]