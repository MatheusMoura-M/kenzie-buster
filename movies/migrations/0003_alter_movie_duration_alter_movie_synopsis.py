# Generated by Django 4.1.6 on 2023-02-14 18:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0002_alter_movie_duration_alter_movie_synopsis"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="duration",
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="movie",
            name="synopsis",
            field=models.TextField(null=True),
        ),
    ]