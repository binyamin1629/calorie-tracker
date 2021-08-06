from django import forms
from .models import BodyStatus



class CreateBodyStatsForm(forms.ModelForm):



    class Meta:
        model=BodyStatus
        fields=['male','weight','hiegth','age','female']
        weight = forms.EmailField(required=True)
        hiegth = forms.EmailField(required=True)
        age = forms.EmailField(required=True)   
         
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['male']=forms.BooleanField(widget=forms.CheckboxInput(attrs={'id':'male'}))
        #self.fields['female']=forms.BooleanField(widget=forms.CheckboxInput(attrs={'id':'female'}))
        # for field in self.fields:
        #     self.fields[field].required = True   
