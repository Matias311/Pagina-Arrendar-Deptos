# Generated by Django 5.1.1 on 2024-09-23 04:11

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('m7_python', '0013_alter_detalle_usuario_tipo_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_contacto', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('email', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('mensaje', models.TextField(max_length=500)),
            ],
        ),
    ]
