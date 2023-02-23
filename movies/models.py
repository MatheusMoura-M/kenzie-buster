from django.db import models


class ParentalIndication(models.TextChoices):
    PG = "PG"
    PG_13 = "PG-13"
    R = "R"
    NC_17 = "NC-17"
    DEFAULT = "G"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True)
    rating = models.CharField(
        max_length=20,
        choices=ParentalIndication.choices,
        default=ParentalIndication.DEFAULT,
    )
    synopsis = models.TextField(null=True)

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="movies"
    )

    ordered_by = models.ManyToManyField(
        "users.User", through="movies.MovieOrder", related_name="ordered_movie"
    )


class MovieOrder(models.Model):
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="purchase_info"
    )
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name="purchase_info"
    )

    price = models.DecimalField(max_digits=8, decimal_places=2)
    buyed_at = models.DateTimeField(auto_now_add=True)
