from django.db import models


class Apartment(models.Model):
    address = models.CharField(max_length=80)
    price = models.CharField(max_length=10)


class Question(models.Model):
    question_name = models.CharField(max_length=25)
    question_text = models.TextField()
    answer_first = models.CharField(max_length=20)
    answer_last = models.CharField(max_length=20)


class Apartment_Question(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    real_value = models.CharField(max_length=50)
    expert_score = models.FloatField()
