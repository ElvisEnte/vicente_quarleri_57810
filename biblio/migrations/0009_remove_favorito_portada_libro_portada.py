# Generated by Django 5.0.7 on 2024-07-20 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblio', '0008_alter_favorito_anio_alter_favorito_genero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorito',
            name='portada',
        ),
        migrations.AddField(
            model_name='libro',
            name='portada',
            field=models.ImageField(blank=True, null=True, upload_to='portadas/'),
        ),
    ]