# Generated by Django 3.2 on 2022-02-15 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distributeur', '0028_alter_créerfacture_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendeur',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]