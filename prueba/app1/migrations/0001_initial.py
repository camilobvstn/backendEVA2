# Generated by Django 3.2 on 2024-10-28 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=15)),
                ('nombreo', models.CharField(max_length=15)),
                ('apellido', models.CharField(max_length=15)),
                ('edad', models.IntegerField(max_length=15)),
            ],
        ),
    ]
