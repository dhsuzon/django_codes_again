from django import forms
from django.core import validators


class ContactForm(forms.Form):
    name = forms.CharField(label="UserName",initial="Suzon",required=False,help_text="Enter Your Name",widget=forms.Textarea(attrs={'rows':5,"cols":5,"class":"class1 class2",
    "placeholder":"Enter your name"}))
    # File = forms.FileField()
    Email = forms.EmailField()
    weight = forms.FloatField()
    Balance = forms.DecimalField()
    Age = forms.CharField(widget=forms.NumberInput)
    Check = forms.BooleanField()
    Birthday = forms.CharField(widget=forms.DateInput(attrs={'type':"date"}))
    Appoinment_date = forms.CharField(widget=forms.DateTimeInput(attrs={'type':"datetime-local"}))
    CHOICES = [("S",'Small'),("M",'Medium'),("L",'Large')]
    Size = forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)
    Meal = [("P","Pepperoni"),("M",'Mashroom'),("B",'Beef')]
    Pizza = forms.MultipleChoiceField(choices=CHOICES,widget=forms.CheckboxSelectMultiple)
    
    
    
    
    
# class StudentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)
#     def clean(self):
#         cleaned_data = super().clean()
#         print(cleaned_data)
#         valname = cleaned_data.get('name')
#         valemail = cleaned_data.get("email")
       
#         if len(valname) < 10:
#             raise forms.ValidationError("Name must be at least 10 characters long.")
 
#         if ".com" not in valemail:
#             raise forms.ValidationError("include must be .com.")
        
class StudentData(forms.Form):
    name = forms.CharField(widget=forms.TextInput,validators=[validators.MaxLengthValidator(10,"Name Highest at least 10 characters long."),validators.MinLengthValidator(5,"Name must be at least 5 characters long")])
    email = forms.CharField(widget=forms.EmailInput,validators=[validators.EmailValidator(message="enter your email address")])
    age = forms.IntegerField(validators=[validators.MaxValueValidator(60,message="age at highest 60 year old"),validators.MinValueValidator(18,message="age at least 18 years old")])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=["png","jpg"],message="file extension support must be jpg,png")])
            