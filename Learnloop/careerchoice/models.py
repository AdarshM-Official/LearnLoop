# Create your models here.
from django.db import models

class Question(models.Model):
    QUESTION_TYPES = [
        ('single-choice', 'Single Choice'),
        ('multiple-choice', 'Multiple Choice'),
    ]
    text = models.CharField(max_length=255)
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES, default='single-choice')

    def __str__(self):
        return self.text

class Option(models.Model):
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.question.text[:30]}... -> {self.text}"

class Response(models.Model):
    # We can use the session key for anonymous users
    session_key = models.CharField(max_length=40)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(Option, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Response to '{self.question.text[:30]}...' by {self.session_key}"