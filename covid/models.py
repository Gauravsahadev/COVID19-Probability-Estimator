from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.
class Coviddata(models.Model):
    age= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    gender= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    fever= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    cough= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    fatigue= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    pains= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    nasal_congestion= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    shortness_of_breath= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    runny_nose= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    sore_throat= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    diarrhea= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    chills= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    headache= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    vomiting= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    lives_in_affected_area= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    result= models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
