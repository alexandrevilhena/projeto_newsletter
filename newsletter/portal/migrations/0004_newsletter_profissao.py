# Generated by Django 5.0.3 on 2024-04-09 02:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_alter_vagaemprego_data_publicacao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='profissao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portal.infosprofissao'),
        ),
    ]
