from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
from .models import UserManager

class StaffRegForm (UserCreationForm):

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-user','placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-user','placeholder':'Confirm Password'}))
    username = forms.CharField(help_text="<p class='text-danger lead'>Maximum of 6 Characters, Minimum of 5</p>",widget=forms.TextInput(attrs={'class':'form-control form-control-user','placeholder':'Instructors username','maxlength':'9','minlength':'7'}))
    is_teacher = forms.CharField(widget=forms.HiddenInput(attrs={'value':'1'}))
    class Meta:
        model = get_user_model()
        fields = ('first_name','last_name','email','username','password1','password2','mobile_number','office','image','is_teacher')
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control form-control-user','placeholder':'First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control form-control-user','placeholder':'Last Name'}),
            'email':forms.TextInput(attrs={'class':'form-control form-control-user','placeholder':'E-mail Address'}),
            'mobile_number':forms.TextInput(attrs={'class':'form-control form-control-user','placeholder':' Mobile Number'}),
            'office':forms.TextInput(attrs={'class':'form-control form-control-user','placeholder':'Office Address'}),
            'image':forms.ClearableFileInput(attrs={'class':'form-control'})

        }
        

class StaffLoginForm(AuthenticationForm):
    
    username = forms.CharField(help_text="<p class='text-danger lead'>Maximum of 6 Characters, Minimum of 5</p>",widget=forms.TextInput(attrs={'class':'form-control form-control-user','placeholder':'Instructor username','maxlength':'9','minlength':'7'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-user', 'placeholder':'Valid Password '}))

    class Meta:
        model=get_user_model()
        fields = ('username','password')


class StudentRegForm (UserCreationForm):

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-user','placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-user','placeholder':'Confirm Password'}))
    is_student = forms.CharField(widget=forms.HiddenInput(attrs={'value':'1'}))
    username = forms.CharField(label='Matric Number',max_length=14, min_length=11, widget=forms.TextInput(attrs={'class':'form-control form-control-user','placeholder':'Student Matric Number'}))
    class Meta:
        model = get_user_model()
        fields = ('first_name','last_name','email','username','password1','password2','prev_result','level','image','is_teacher')
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control form-control-user','placeholder':'First Name','required':'required'}),
            'last_name':forms.TextInput(attrs={'class':'form-control form-control-user','placeholder':'Last Name','required':'required'}),
            'email':forms.TextInput(attrs={'class':'form-control form-control-user','placeholder':'E-mail Address','required':'required'}),
            #'username':forms.TextInput(attrs={'class':'form-control form-control-user','placeholder':'Student username'}),
            'level':forms.Select(attrs={'class':'form-control','placeholder':'Level','required':'required'}),
            'prev_result':forms.Select(attrs={'class':'form-control','value':'Previous Result','required':'required'}),
            'image':forms.ClearableFileInput(attrs={'class':'form-control','required':'required'})

        }


class StudentLoginForm(AuthenticationForm):
    
    username = forms.CharField(help_text="<p class='text-danger lead'>Maximum of 14 Characters, Minimum of 11</p>",widget=forms.TextInput(attrs={'class':'form-control form-control-user','required':'required','placeholder':'Student Matric Number','maxlength':'14','minlength':'11'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-user', 'required':'required', 'placeholder':'Valid Password '}))
    # level = forms.ChoiceField(choices=UserManager.choice,  widget=forms.Select(attrs={'class':'form-control form-control-user'}))
    # prev_result = forms.ChoiceField(choices=UserManager.result,label='Current Grade',widget=forms.Select(attrs={'class':'form-control form-control-user'}))

    class Meta:
        model=get_user_model()
        fields = ('username','password')

   
class Instructor_Profile(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name','last_name','username','email','mobile_number','image')

        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'last_name':forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'username':forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'email':forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'mobile_number':forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'image':forms.ClearableFileInput(attrs={'class':'form-control form-control-user'}),
        }

class Student_Profile(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name','last_name','username','email','mobile_number','image')

        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'last_name':forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'username':forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'email':forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'mobile_number':forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'image':forms.ClearableFileInput(attrs={'class':'form-control form-control-user'}),
        }