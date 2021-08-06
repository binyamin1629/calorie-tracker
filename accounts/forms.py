from django import forms
from .models import Account


class RgisterForm(forms.ModelForm):

    password=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter password...',
    }))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Confirm password...',
    }))
    
    class Meta:
        model = Account
        fields=['first_name','last_name','email','password','profile_image']

    def __init__(self,*args,**kwargs):
        super(RgisterForm, self).__init__(*args,*kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='rgisterlogininput'
            

    def clean(self):
        cleaned_data=super(RgisterForm,self).clean()
        password=cleaned_data.get('password')
        confirm_password=cleaned_data.get('confirm_password') 
        if(password!=confirm_password):
            raise forms.ValidationError(
            'password dose not match!!!'
        )
         

class EditForm(forms.ModelForm):

    class Meta:

        model = Account
        fields=['first_name','last_name','email','profile_image']



    # def __init__(self,*args,**kwargs):
        
    #     super(EditForm, self).__init__(*args,*kwargs)
    #     for editfield in self.fields:
    #        self.fields[editfield].widget.attrs['class']='rgisterlogininput'