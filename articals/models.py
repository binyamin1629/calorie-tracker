from django.db import models
from accounts.models import Account
# Create your models here.
class Post(models.Model): 
    
    authur              =models.ForeignKey(Account,on_delete=models.CASCADE)
    title               =models.CharField(max_length=100)
    article             =models.TextField()
    article_image       =models.ImageField(upload_to='photos/article',blank=True)
    published           =models.DateTimeField(auto_now=True)


    def __str__(self):
        return  self.title