# Generated by Django 4.2.5 on 2023-09-29 16:25

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Publicacao",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "titulo",
                    models.CharField(help_text="Entre o titulo", max_length=100),
                ),
                (
                    "texto",
                    models.CharField(
                        help_text="Digite o texto da publicacao", max_length=10000
                    ),
                ),
            ],
        ),
    ]