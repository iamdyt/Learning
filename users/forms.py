from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model

class StaffRegForm (UserCreationForm):

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-user','placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-user','placeholder':'Confirm Password'}))
    is_teacher = forms.CharField(widget=forms.HiddenInput(attrs={'value':'1'}))
    class Meta:
        model = get_user_model()
        fields = ('first_name','last_name','email','username','password1','password2','mobile_number','office','image','is_teacher')
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control form-control-user','placeholder':'First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control form-control-user','placeholder':'Last Name'}),
            'email':forms.TextInput(attrs={'class':'form-control form-control-user','placeholder':'E-mail Address'}),
            'username':forms.TextInput(attrs={'class':'form-control form-control-user','placeholder':'Instructors username'}),
            'mobile_number':forms.TextInput(attrs={'class':'form-control form-control-user','placeholder':' Mobile Number'}),
            'office':forms.TextInput(attrs={'class':'form-control form-control-user','placeholder':'Office Address'}),
            'image':forms.ClearableFileInput(attrs={'class':'form-control'})

        }
class StaffLoginForm(AuthenticationForm):
    
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-user','placeholder':'Instructor username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-user', 'placeholder':'Valid Password '}))

    class Meta:
        model=get_user_model()
        fields = ('username','password')
        
