from django.shortcuts import render,redirect
from .forms import RgisterForm,EditForm
from .models import Account
from django.contrib import messages,auth
# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    else:

        if request.method=='POST':

            form=RgisterForm(request.POST,request.FILES)
            if form.is_valid():
                first_name=form.cleaned_data['first_name']
                last_name=form.cleaned_data['last_name']
                email=form.cleaned_data['email']
                password=form.cleaned_data['password']
                profile_image=form.cleaned_data['profile_image']
                username=email.split('@')[0]



            user=Account.objects.create_user(first_name=first_name,last_name=last_name
            ,username=username,email=email,password=password,profile_image=profile_image)
            
            user.save()
            messages.error(request,'user name or password is incorrect')
            return redirect('login')
        else:
            form=RgisterForm()

    context={
         'form':form
     }   
    return render(request,'accounts/register.html',context)









def login(request):

    if request.user.is_authenticated:
        return redirect('home')
    else:
        
        message=''
        if request.method=='POST':


            email=request.POST['email']
            password=request.POST['password']

            user=auth.authenticate(email=email,password=password)

            if user is not None:
                auth.login(request,user)
                return redirect('home')
            
            else:


                messages.error(request,'Invalid email or password!!!')
                message='Invalid email or password!!!'
        return render(request,'accounts/login.html',{'message':message})




    






def logout(request):
    auth.logout(request)

    return redirect('home')


def profileDetails(request,pk):
    #get user 
    user=Account.objects.get(id=pk)
    context={
         'user':user
    } 
    
    return render(request,'accounts/profileDetails.html',context)

def editprofile(request,pk):

    user=Account.objects.get(id=pk)
    editform=EditForm(instance=user)
    if request.method=='POST':
        editform=EditForm(request.POST,request.FILES,instance=user)
  
        if editform.is_valid(): 
            

            editform.save()
            return redirect('profileDetails',pk=user.id)   
    
    context={
         'editform':editform
    }


    return render(request,'accounts/editProfile.html',context)

   
    
            #checked=editform.cleaned_data['profile_image-clear']
            # if checked:
            #     instance=editform(commit=False)
            #     instance.profile_image=None

            # instance=editform(commit=False)
            # instance.profile_image=Nones
        