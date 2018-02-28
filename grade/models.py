from django.db import models
# Create your models here.
class Grade(models.Model):
    basic_seminar          = models.DecimalField(max_digits=2, decimal_places=1,default=0)
    language_english       = models.DecimalField(max_digits=2, decimal_places=1,default=0)
    sport                  = models.DecimalField(max_digits=2, decimal_places=1,default=0)
    human_basic            = models.DecimalField(max_digits=2, decimal_places=1,default=0)
    science_basic_human    = models.DecimalField(max_digits=2, decimal_places=1,default=0)
    science_basic_science  = models.DecimalField(max_digits=2, decimal_places=1,default=0)
    liberal_human          = models.DecimalField(max_digits=2, decimal_places=1,default=0)
    liberal_science        = models.DecimalField(max_digits=2, decimal_places=1,default=0)
    liberal_all            = models.DecimalField(max_digits=2, decimal_places=1,default=0)
    liberal_free           = models.DecimalField(max_digits=2, decimal_places=1,default=0)
    major                  = models.DecimalField(max_digits=2, decimal_places=1,default=0)

    def __str__(self):
        return str(self.pk)
