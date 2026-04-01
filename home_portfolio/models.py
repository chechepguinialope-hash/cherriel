from django.db import models

class Skills(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(help_text='Proficiency of the skill(85%): ')

    def __str__(self):
        return self.name

# Create your models here.
