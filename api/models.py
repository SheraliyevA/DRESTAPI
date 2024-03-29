from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User

class Mundarija(Model):
    mavzu=models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.mavzu

class Mashqlar(Model):
    title=models.CharField(max_length=200,blank=True,null=True)
    body=models.TextField(db_index=True)
    created=models.DateTimeField(auto_now_add=True)
    youtobe=models.CharField(max_length=2000,blank=True,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='questions')
    theme=models.ForeignKey(Mundarija,on_delete=models.CASCADE,related_name='themes')

    def __str__(self):
        return f"{self.title[:40]}"

class Comment(Model):
    comment_count=models.PositiveIntegerField(verbose_name='comment count')
    created=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    question=models.ForeignKey(Mashqlar,on_delete=models.CASCADE)

    def __str__(self):
        return "{}-{}".format(self.comment_count,(self.user))