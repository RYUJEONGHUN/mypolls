from django.utils import timezone  # Django의 timezone 모듈을 가져옵니다.
from datetime import timedelta  # timedelta만 datetime에서 가져옵니다.
from django.db import models

class Question(models.Model):
  question_text=models.CharField(max_length=200)
  pub_date=models.DateTimeField('date published')
  
  def __str__(self):
    return self.question_text
  
  def was_published_recently(self):
    return timezone.now()>=self.pub_date >= timezone.now()-timedelta(days=1)
  was_published_recently.admin_order_field='pub_date'
  was_published_recently.boolean=True
  was_published_recently.short_description='Published recently?'

class Choice(models.Model):
  question=models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text=models.CharField(max_length=200)
  votes=models.IntegerField(default=0)

  def __str__(self):
    return self.choice_text
# Create your models here.
