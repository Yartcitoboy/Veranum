# Generated by Django 5.1.3 on 2024-11-23 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicaciones', '0004_alter_contacto_rut'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('rut', models.CharField(max_length=10, unique=True)),
                ('email', models.CharField(max_length=120)),
                ('password', models.CharField(max_length=128)),
                ('sexo', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='contacto',
            name='comuna',
        ),
        migrations.DeleteModel(
            name='Comuna',
        ),
        migrations.DeleteModel(
            name='Contacto',
        ),
    ]
