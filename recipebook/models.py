from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class recipes(models.Model):
    User = models.ForeignKey(User , on_delete=models.SET_NULL,null=True,blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image= models.ImageField(upload_to="img")
    created_at = models.DateTimeField(auto_now_add=True)
    