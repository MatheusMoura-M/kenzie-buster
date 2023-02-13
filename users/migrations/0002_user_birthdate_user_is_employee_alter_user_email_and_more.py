# Generated by Django 4.1.6 on 2023-02-13 17:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="birthdate",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="is_employee",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.CharField(max_length=127, unique=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(max_length=50),
        ),
    ]
