# Generated by Django 5.0.3 on 2024-12-29 18:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("escola", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Matricula",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "periodo",
                    models.CharField(
                        choices=[
                            ("M", "Matutino"),
                            ("V", "Vespertino"),
                            ("N", "Noturno"),
                        ],
                        default="M",
                        max_length=1,
                    ),
                ),
                ("nota", models.DecimalField(decimal_places=2, max_digits=5)),
                ("frequencia", models.DecimalField(decimal_places=2, max_digits=5)),
                (
                    "curso",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="escola.curso"
                    ),
                ),
                (
                    "estudante",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="escola.estudante",
                    ),
                ),
            ],
        ),
    ]
