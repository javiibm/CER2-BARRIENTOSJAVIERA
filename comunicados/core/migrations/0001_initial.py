# Generated by Django 3.2.9 on 2023-06-07 22:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=20)),
                ('descripcion', models.TextField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Comunicado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField(max_length=20)),
                ('detalle', models.TextField(max_length=40)),
                ('nivel', models.CharField(choices=[('GEN', 'General'), ('PRE', 'Ciclo Preescolar'), ('BAS', 'Ciclo Básico'), ('MED', 'Ciclo Medio')], max_length=20)),
                ('fecha_envio', models.DateTimeField()),
                ('fecha_ultima_modificacion', models.DateTimeField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
                ('publicado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
