# Generated by Django 4.2.5 on 2023-09-09 07:12

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('ativo', models.BooleanField(default=True)),
                ('nome', models.CharField(max_length=70)),
                ('endereco', models.CharField(max_length=150)),
                ('bairro', models.CharField(max_length=50)),
                ('cep', models.CharField(max_length=9)),
                ('cidade', models.CharField(max_length=200)),
                ('estado', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Especie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('ativo', models.BooleanField(default=True)),
                ('descricao', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Espécie',
                'verbose_name_plural': 'Espécies',
            },
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('ativo', models.BooleanField(default=True)),
                ('nome', models.CharField(max_length=70)),
                ('idade', models.CharField(max_length=150)),
                ('sexo', models.CharField(max_length=9)),
                ('foto', stdimage.models.StdImageField(force_min_size=False, upload_to='animais', variations={'thumb': {'crop': True, 'height': 600, 'width': 600}})),
                ('idCliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.cliente')),
                ('idEspecie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.especie')),
            ],
            options={
                'verbose_name': 'Animal',
                'verbose_name_plural': 'Animais',
            },
        ),
    ]
