# Generated by Django 4.1.7 on 2023-05-05 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('our_shop', '0002_commande'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commande',
            options={'ordering': ['-date_Commande']},
        ),
    ]
