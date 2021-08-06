from django.db import models
from accounts.models import Account
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class BodyStatusManager(models.Manager):
    def Create_stats(self,user,male,weight,hiegth,age):
        totoalCaloriesPerDay=dayli_calorie(weight,hiegth,male,age)
        body_stats=self.model(
            user=user,
            male=male,

            
            weight=weight,
            hiegth=hiegth,
            age=age
        )
        body_stats.totoalCaloriesPerDay=dayli_calorie(weight,hiegth,male,age)
        body_stats.save(using=self._db)
        return body_stats
    
class BodyStatus(models.Model):

    
    user         =models.ForeignKey(Account,on_delete=models.CASCADE)
    male         =models.BooleanField(default=True)
    female         =models.BooleanField(default=False)
    totoalCaloriesPerDay = models.IntegerField(blank=True,null=True)
    weight       =models.IntegerField(default=40,validators=[MaxValueValidator(250), MinValueValidator(40)])
    hiegth       =models.IntegerField(default=160,validators=[MaxValueValidator(250), MinValueValidator(160)])
    dateChange   =models.DateTimeField(auto_now=True)
    age          =models.IntegerField(default=18,validators=[MaxValueValidator(99), MinValueValidator(18)])  
    objects      =BodyStatusManager()
    def __str__(self):
        return  'your totla claos is ' +str(self.totoalCaloriesPerDay)


def  dayli_calorie(weight,hiegth,male,age):

    print(f"{male} is a powerful technique")
    weightInKilo=weight/2.2
    hiegthIncentimeters=hiegth*2.54
    bmr=0
    
        
    if male:
        bmr= int((10*weightInKilo)+(6.25*hiegthIncentimeters)-(5*age)+5)
        return bmr
    else:
        bmr= int((10*weightInKilo)+(6.25*hiegthIncentimeters)-(5*age)-161)
        print(f"{bmr} bmr is ")
        return bmr
        
        
        
        
        
        

    
    
    

