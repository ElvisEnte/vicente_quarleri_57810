# Generated by Django 5.0.7 on 2024-07-20 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblio', '0007_favorito_delete_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorito',
            name='anio',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='favorito',
            name='genero',
            field=models.CharField(max_length=50),
        ),
    ]
