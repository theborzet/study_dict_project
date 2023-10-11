from django.db import models

class Word(models.Model):
    english = models.CharField(max_length=128, unique=True)
    translate = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return f'{self.english} - {self.translate}'
