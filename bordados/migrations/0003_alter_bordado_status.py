# Generated by Django 4.2.4 on 2023-08-07 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bordados', '0002_bordado_quantidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bordado',
            name='status',
            field=models.CharField(choices=[('Na Loja', 'Na Loja'), ('Bordando', 'Bordando'), ('Concluído', 'Concluído')], max_length=20),
        ),
    ]
