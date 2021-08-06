from django.db import models
from accounts.models import Account 

# Create your models here.
class calosPerDayManager(models.Manager):
    def InsertCalosPerDay(self,total_calos,date_of_meal,user):
        total=self.model(
            total_calos=total_calos,
            date_of_meal=date_of_meal,
            user=user

        )
        total.save(using=self._db)
        return total 







class calosManager(models.Manager):
    def createAndSetCalos(self,calos,meal,user):
        calories=self.model(
            calos=calos,
            meal=meal,
            user=user
        )
        calories.save(using=self._db)
        return calories        




class myMealManager(models.Manager):
    def Create_Meal(self,mealType,user):
        
        meal=self.model(
            user=user,
            mealType=mealType,
            
           
         
        )
        
        meal.save(using=self._db)
        return meal


class FoodInlMaelManager(models.Manager):
    def CreateFoodInMeal(self,food_id,meal_id):

        
        fdinmeal=self.model(
            food_id=food_id,
            meal_id=meal_id,
        
        )

        
        fdinmeal.save(using=self._db)
        return fdinmeal


class FoodManager(models.Manager):
    def CreateFood(self,calories,protien,fat,carbs,foodName):

        
        food=self.model(
            calories=calories,
            protien=protien,
            fat=fat,
            carbs=carbs,
            foodName=foodName
           
         
        )
        
        food.save(using=self._db)
        return food        



class mealTypes(models.Model):
    title           =models.CharField(max_length=200,unique=True)
    slug            =models.SlugField(max_length=255,unique=True)
    image           =models.ImageField(upload_to='photos',blank=True)

    def __str__(self):
        return self.title



class MyMeal(models.Model):
    mealType        =models.ForeignKey(mealTypes,on_delete=models.CASCADE)
    user            =models.ForeignKey(Account,on_delete=models.CASCADE)
    
    mealDate    =models.DateField(auto_now_add=True)
    objects     =myMealManager()
    def __str__(self):
        return str(self.mealType.title)

class food(models.Model):
    calories    =models.CharField(max_length=200)
    protien     =models.CharField(max_length=200)
    fat         =models.CharField(max_length=200)
    carbs       =models.CharField(max_length=200)
    foodName    =models.CharField(max_length=200)
    objects      =FoodManager()
    def __str__(self):
        return self.foodName
    



class foodInMeal(models.Model):
    food_id        =models.ForeignKey(food,on_delete=models.CASCADE)
    meal_id        =models.ForeignKey(MyMeal,on_delete=models.CASCADE)
    
    objects      =FoodInlMaelManager()



    def __str__(self):
        return 'new food'
  
    
class totalCalosPerMeal(models.Model):
    calos       =models.FloatField()
    meal        =models.ForeignKey(MyMeal,on_delete=models.CASCADE)               
    user        =models.ForeignKey(Account,on_delete=models.CASCADE)
    dateOfMeal    =models.DateField(auto_now_add=True)
    objects     =calosManager()
    def __str__(self):
        return str(self.calos)

class totalCalosPerDay(models.Model):
    total_calos     =models.FloatField()
    date_of_meal    =models.DateField(auto_now_add=True)
    user            =models.ForeignKey(Account,on_delete=models.CASCADE)   
    objects         =calosPerDayManager()
   
    def __str__(self):
        return str(self.total_calos)
       