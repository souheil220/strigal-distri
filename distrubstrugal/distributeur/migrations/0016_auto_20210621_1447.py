# Generated by Django 3.2 on 2021-06-21 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distributeur', '0015_auto_20210616_0758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='active',
        ),
        migrations.RemoveField(
            model_name='article',
            name='categorie_interne',
        ),
        migrations.RemoveField(
            model_name='article',
            name='company_id',
        ),
        migrations.RemoveField(
            model_name='article',
            name='famille_article',
        ),
        migrations.RemoveField(
            model_name='article',
            name='sale_ok',
        ),
        migrations.RemoveField(
            model_name='article',
            name='template_id',
        ),
        migrations.RemoveField(
            model_name='article',
            name='type_article',
        ),
        migrations.RemoveField(
            model_name='article',
            name='type_de_categorie',
        ),
        migrations.AlterField(
            model_name='commande',
            name='date',
            field=models.CharField(default='2021-06-21', max_length=255),
        ),
    ]