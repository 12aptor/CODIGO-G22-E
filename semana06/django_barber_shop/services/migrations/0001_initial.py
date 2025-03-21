# Generated by Django 5.1.6 on 2025-03-01 03:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BarberModel",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=100, unique=True)),
                ("phone", models.CharField(max_length=20, unique=True)),
                ("speciality", models.CharField(max_length=100)),
                ("status", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "barbers",
            },
        ),
        migrations.CreateModel(
            name="ServiceModel",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("price", models.IntegerField()),
                ("duration", models.IntegerField()),
            ],
            options={
                "db_table": "services",
            },
        ),
        migrations.CreateModel(
            name="ScheduleModel",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "day_of_week",
                    models.CharField(
                        choices=[
                            ("MONDAY", "MONDAY"),
                            ("TUESDAY", "TUESDAY"),
                            ("WEDNESDAY", "WEDNESDAY"),
                            ("THURSDAY", "THURSDAY"),
                            ("FRIDAY", "FRIDAY"),
                            ("SATURDAY", "SATURDAY"),
                            ("SUNDAY", "SUNDAY"),
                        ],
                        max_length=10,
                    ),
                ),
                ("start_time", models.TimeField()),
                ("end_time", models.TimeField()),
                (
                    "barber",
                    models.ForeignKey(
                        db_column="barber_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="schedules",
                        to="services.barbermodel",
                    ),
                ),
            ],
            options={
                "db_table": "schedules",
            },
        ),
    ]
