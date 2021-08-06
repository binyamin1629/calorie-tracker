from django.shortcuts import render,redirect
from .models import mealTypes,MyMeal,food,foodInMeal,totalCalosPerMeal,totalCalosPerDay
from accounts.models import Account
from bodystats.models import BodyStatus
import requests
import json
from django.utils import timezone
import datetime
from django.urls import reverse
from django.http import HttpResponseRedirect
from calendar import monthrange,HTMLCalendar
import calendar
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def get_all_mealTypes(request,pk):

    meal_types=mealTypes.objects.all()

    context={
        'meal_types':meal_types
    }

    return render(request,'meal/mealTypes.html',context)









@login_required(login_url='login')
def createmeal(request,mealTypeResult,pk):

    user=Account.objects.get(id=pk)
    currentDate=datetime.date.today()
    try:
        total_calos_per_day=totalCalosPerDay.objects.get(user=user,date_of_meal=currentDate)
    except totalCalosPerDay.DoesNotExist:
        total_calos_per_day=totalCalosPerDay.objects.InsertCalosPerDay(0,currentDate,user)
        
    
    query=''
    totalPerDayCals=0
    message=''
    cals=0
    totalClos=0
    mealType=mealTypes.objects.get(slug=mealTypeResult)
    meal=''
    date = datetime.date.today()
    try:
       meal=MyMeal.objects.get(mealType=mealType,mealDate=date,user=user)
    except MyMeal.DoesNotExist:
        meal=MyMeal.objects.Create_Meal(mealType,user)
        
    dateOf_Meal=meal.mealDate
    name=''
    fooddata=''
    if request.method=='POST':
        searchObj=request.POST.get('query')
        
        
        api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
        query = searchObj
        response = requests.get(api_url + query, headers={'X-Api-Key': 'W3OCazw0Qb46C0iLR5J37g==CflGjDutZmtCeNSL'})
        if response.status_code == requests.codes.ok:

            fooddata=json.loads(response.text)
        for data in fooddata['items']:
            name=data['name']
            carbs=data['carbohydrates_total_g']
            protien=data['protein_g']
            fat=data['fat_total_g']
            calos=data['calories']
            singlefood=food.objects.CreateFood(calos,protien,fat,carbs,name)
            

            cals=cals+float(calos)
            foods=foodInMeal.objects.CreateFoodInMeal(singlefood,meal)




        else:
            fooddata=response.text
            if  response.status_code==200:

                message='No Food Was Found!!!'
                print("Error:", response.status_code, response.text)


    #mealdate=foodInMeal.objects.filter(meal_id.mealDate == currentDate)       
    foods_data=foodInMeal.objects.filter(meal_id=meal,meal_id__user=user)
    #mealdate=foods_data.mealDate
    for calorie in foods_data:
        totalPerDayCals=totalPerDayCals+float(calorie.food_id.calories)

    try:
        totalClos=totalCalosPerMeal.objects.get(meal=meal)
        totalClos.calos=totalPerDayCals 
        totalClos.save()

    except totalCalosPerMeal.DoesNotExist:
        totalClos=totalCalosPerMeal.objects.createAndSetCalos(totalPerDayCals,meal,request.user)







    context={
            'mealTypeResult':mealTypeResult,         
            'name':name,
            'message':message,
            'foods_data':foods_data
    }
      

   

    return render(request,'meal/createMeal.html',context)


def removeFood(request,mealTypeResult,foodInMeal_id):
    #find the meal type:

    food_id=food.objects.get(id=foodInMeal_id)
    food_id.delete()


    return redirect(reverse('createmeal' ,args=[mealTypeResult,request.user.id]))









def deatilsByDate(request,pk):
    user=Account.objects.get(id=pk)
    try:


        body__status=BodyStatus.objects.get(user=user)
        
    except BodyStatus.DoesNotExist:
        return redirect('cratebodystats',pk=user.id)
        
   
    meal=MyMeal.objects.filter(user=user)
    totalCalosPer_Meal=totalCalosPerMeal.objects.filter(user=user)
    calosPerDay=0
    num=0
    calos__per__day=0
    currentDate=datetime.date.today()

    
    bodystatusCalos=BodyStatus.objects.get(user=user).totoalCaloriesPerDay
    

    foods_data=foodInMeal.objects.filter(meal_id__mealDate=currentDate)

    for dayCalos in foods_data:
        calos__per__day=calos__per__day+float(dayCalos.food_id.calories)

  
    total=totalCalosPerDay.objects.get(user=user,date_of_meal=currentDate)
    # total.total_calos=calos__per__day
    total.delete()
    
  
  

    total=totalCalosPerDay.objects.InsertCalosPerDay(calos__per__day,currentDate,request.user)
    getCalos=totalCalosPerDay.objects.filter(user=user)

    context={
        'user':user,
        'meal':meal,
        'getCalos':getCalos,
        'currentDate':currentDate,
        'bodystatusCalos':bodystatusCalos,
     
        
    }

    
    return render(request,'meal/dateDetails.html',context)


def typeofmaelDetails(request,date,pk):
    meal_types=mealTypes.objects.all()
    getCalos=totalCalosPerDay.objects.get(date_of_meal=date)
    

    context={
        'meal_types':meal_types,
        'date':date,
        'getCalos':getCalos
    }


    return render(request,'meal/mealTypeDaetails.html',context)

def detailsOfDay(request,date,mealType,pk):
    meal_type=mealTypes.objects.get(slug=mealType)
    user=Account.objects.get(id=pk)
    foods_data=foodInMeal.objects.filter(meal_id__mealDate=date,meal_id__mealType=meal_type,meal_id__user=user)
    #try expcept
    # mealId=foods_data[0].meal_id.id
    # meal=MyMeal.objects.get(id=mealId)
    try:
        total_calos_per_meal=totalCalosPerMeal.objects.get(dateOfMeal=date,meal__mealType=meal_type)
    except totalCalosPerMeal.DoesNotExist:
        total_calos_per_meal=0.0
        


    context={
        'foods_data':foods_data,
        'meal_type':meal_type,
        'total_calos_per_meal':total_calos_per_meal
    }
    return render(request,'meal/detailsperday.html',context)


