# Generated by Django 5.1.1 on 2024-09-18 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('m7_python', '0008_alter_inmueble_id_inmueble'),
    ]

    operations = [
        migrations.AddField(
            model_name='inmueble',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='id_inmueble',
            field=models.CharField(max_length=2, primary_key=True, serialize=False),
        ),
    ]
