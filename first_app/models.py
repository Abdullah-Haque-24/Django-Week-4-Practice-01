from django.db import models

# Create your models here.
class MyModel(models.Model):
    #Practice Day 01
    big_integer_field = models.BigIntegerField()
    big_integer_field = models.BigIntegerField()
    binary_field = models.BinaryField()
    boolean_field = models.BooleanField()
    char_field = models.CharField(max_length=255)
    # comma_separated_field = models.CharField(
    #     validators=[comma_separated_validator],
    #     max_length=255
    # )
    date_field = models.DateField()
    date_time_field = models.DateTimeField()
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    positive_big_integer_field = models.PositiveBigIntegerField()
    slug_field = models.SlugField()
    time_field = models.TimeField()
    text_field = models.TextField()








































    ##########################################################################################
    # name = models.CharField(max_length = 100)
    # bio = models.TextField()
    # phone_no = models.CharField(max_length = 12)

    # def __str__(self):
    #     return self.name