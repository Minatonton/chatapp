from django.db import models
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    image = models.ImageField("プロフィール画像", upload_to='media_local',blank=True,null=True)
class Talk_model(models.Model):
    message=models.CharField(max_length=100)
    talk_from=models.ForeignKey(CustomUser,on_delete=models.CASCADE, related_name="talk_form")
    talk_to=models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="talk_to")
    talk_time=models.DateTimeField()
