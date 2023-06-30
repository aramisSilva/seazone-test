# Generated by Django 4.2.2 on 2023-06-29 17:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0004_remove_anuncios_data_entrada_and_more'),
        ('reservas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservas',
            old_name='data_entrada',
            new_name='check_in',
        ),
        migrations.RenameField(
            model_name='reservas',
            old_name='data_saida',
            new_name='check_out',
        ),
        migrations.RemoveField(
            model_name='reservas',
            name='inquilino',
        ),
        migrations.AddField(
            model_name='reservas',
            name='codigo_reserva',
            field=models.CharField(default=uuid.uuid4, max_length=200),
        ),
        migrations.AddField(
            model_name='reservas',
            name='comentario',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='reservas',
            name='data_atualizacao',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='reservas',
            name='data_criacao',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservas',
            name='numero_hospedes',
            field=models.PositiveIntegerField(default=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservas',
            name='preco_total',
            field=models.FloatField(default=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reservas',
            name='anuncio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservas', to='anuncios.anuncios'),
        ),
    ]