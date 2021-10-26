from django import forms 
from .models import Portfolio



class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        exclude=[""]
   
        

                
        


class store(forms.Form):
    name= forms.CharField(widget= forms.TextInput(attrs={'class':'form-control','id':'name','placeholder':'Enter your name'}))
    email=forms.EmailField(widget= forms.EmailInput(attrs={'class':'form-control','id':'email','placeholder':'Enter your email'}))
    city= forms.CharField(widget= forms.TextInput(attrs={'class':'form-control','id':'city','placeholder':'Enter your city'}))
    address=forms.CharField(widget= forms.Textarea(attrs={'class':'form-control','id':'address','placeholder':'address'}))
    maritialstatus=forms.CharField(widget= forms.RadioSelect(choices=[('Married', 'Married'),('Unmarried', 'Unmarried'), ('engaged','engaged')]))
    contactno=forms.IntegerField(widget= forms.TextInput(attrs={'class':'form-control','id':'mobile','name':'mobile','placeholder':'Mobile No'}))
    image= forms.ImageField(widget= forms.FileInput(attrs={'class':'form-control','id':'image','name':'image','autofocus':'autofocus'}))
    biodata= forms.FileField(widget= forms.FileInput(attrs={'class':'form-control','id':'document','name':'resume'}))
    date_time=forms.DateTimeField(widget= forms.widgets.DateInput(attrs={'type':'date','class':'form-control','id':'dob','autofocus':'autofocus','placeholder':'Date and Time'}))
    