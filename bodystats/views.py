from django.shortcuts import render ,redirect
from .froms import CreateBodyStatsForm
from accounts.models import Account
from .models import BodyStatus
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def cratebodystats(request,pk):
    form=CreateBodyStatsForm()
    user=Account.objects.get(id=pk)
    try:

        body__status=BodyStatus.objects.get(user=user)
        form=CreateBodyStatsForm(instance=body__status)
    except BodyStatus.DoesNotExist:
        
        body__status=None
        #if body__status is None:
        form=CreateBodyStatsForm()
       



    if request.method=='POST':
        #user=Account.objects.get(id=pk)
        
        form=CreateBodyStatsForm(request.POST)


        if form.is_valid():
  
            
            age=int(form['age'].value())
            weight=int(form['weight'].value())
            hiegth=int(form['hiegth'].value())
            male=bool(form['male'].value())
        
            try:
                body__status=BodyStatus.objects.get(user=user)
                body__status.male=male
  
                body__status.weight=weight
                body__status.hiegth=hiegth
                body__status.age=age
                body__status.totoalCaloriesPerDay=dayli_calorie(weight,hiegth,male,age)
            except BodyStatus.DoesNotExist:
                 body__status=BodyStatus.objects.Create_stats(user,male,weight,hiegth,age)
            print(male)
            #body__status=BodyStatus.objects.Create_stats(user,male,weight,hiegth,age)
            body__status.save()
            return redirect('bodystatusDetails',pk=user.id) 
        
    else:


        contex={
            'form':form
        }
        return render(request,'bodystatus/bodystatuscreate.html',contex)

           
            

   


    

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







def bodystatusDetails(request,pk):
    user=Account.objects.get(id=pk)
    try:
        body__status=BodyStatus.objects.get(user=user)
    except BodyStatus.DoesNotExist:
        body__status=None
        if body__status is None:
            return redirect('cratebodystats',pk=user.id)

    body_status=BodyStatus.objects.get(user=user)





    context={
        'user':user,
        'body_status':body_status,
    }
    return render(request,'bodystatus/bodyStatusDetails.html',context)
