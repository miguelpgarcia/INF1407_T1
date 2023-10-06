# Generated by Django 4.2.5 on 2023-10-06 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("forum", "0002_comentario"),
    ]

    operations = [
        migrations.AddField(
            model_name="publicacao",
            name="autor",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="publicacao",
            name="data_publicacao",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]