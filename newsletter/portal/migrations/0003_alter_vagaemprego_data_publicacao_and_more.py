# Generated by Django 5.0.3 on 2024-04-03 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_rename_materia_chamativa_newsletter_desc_materia_chamativa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vagaemprego',
            name='data_publicacao',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='vagaemprego',
            name='salario',
            field=models.CharField(max_length=255),
        ),
    ]
