from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Breed(models.Model):
    title = models.CharField(
        max_length=32,
        verbose_name='Breed title'
    )

    def __str__(self):
        return f'{self.title}'


class Kitten(models.Model):
    color = models.CharField(
        max_length=64,
        verbose_name='Kitten color'
    )

    age = models.PositiveSmallIntegerField(
        verbose_name='Kitten age'
    )

    description = models.TextField(
        verbose_name='Kitten description'
    )

    breed = models.ForeignKey(
        to=Breed,
        on_delete=models.CASCADE
    )

    owner = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.color} : {self.breed}'

class Rating(models.Model):
    kitten = models.ForeignKey(Kitten, related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])

    class Meta:
        unique_together = ('kitten', 'user')
