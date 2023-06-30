# Generated by Django 4.2.2 on 2023-06-29 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0002_alter_anuncios_preco'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anuncios',
            old_name='data_fim',
            new_name='data_entrada',
        ),
        migrations.RenameField(
            model_name='anuncios',
            old_name='data_inicio',
            new_name='data_saida',
        ),
        migrations.AddField(
            model_name='anuncios',
            name='descricao',
            field=models.TextField(default='Este imóvel está para alugar'),
        ),
        migrations.AlterField(
            model_name='anuncios',
            name='preco',
            field=models.FloatField(),
        ),
    ]