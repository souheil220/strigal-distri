# Generated by Django 3.2 on 2021-06-27 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distributeur', '0017_alter_commande_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='date',
            field=models.CharField(default='2021-06-27', max_length=255),
        ),
    ]