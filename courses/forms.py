from django import forms
from .models import Course,Topic
from django.contrib.auth import get_user_model,get_user


class CreateCourseForm(forms.ModelForm):
    instructor = forms.ModelChoiceField(get_user_model().objects.all(), widget=forms.Select(attrs={'class':'form-control form-control-user'}))
    class Meta:
        model = Course
        fields= '__all__'
        widgets={
            'course_code':forms.TextInput(attrs={'class':'form-control form-control-user','placeholder':'Course Code'}),
            'course_name':forms.TextInput(attrs={'class':'form-control form-control-user','placeholder':'Course name'}),
            'description':forms.Textarea(attrs={'class':'form-control','rows':'3','id':'summernote'}),
            'levels':forms.Select(attrs={'class':'form-control form-control-user','placeholder':''}),
            'level':forms.Select(attrs={'class':'form-control form-control-user','placeholder':''}),
            'session':forms.Select(attrs={'class':'form-control form-control-user','placeholder':''}),
            'semester':forms.Select(attrs={'class':'form-control form-control-user','placeholder':''}),
            'file':forms.FileInput(attrs={'class':'form-control form-control-user'})
        }

class CourseUpdateForm(forms.ModelForm):
   
    class Meta:
        model = Course
        exclude = ['instructor','file']
        widgets={
            'course_code':forms.TextInput(attrs={'class':'form-control form-control-user','placeholder':'Course Code'}),
            'course_name':forms.TextInput(attrs={'class':'form-control form-control-user','placeholder':'Course name'}),
            'description':forms.Textarea(attrs={'class':'form-control','rows':'3','id':'summernote'}),
            'levels':forms.Select(attrs={'class':'form-control form-control-user','placeholder':''}),
            'level':forms.Select(attrs={'class':'form-control form-control-user','placeholder':''}),
            'session':forms.Select(attrs={'class':'form-control form-control-user','placeholder':''}),
            'semester':forms.Select(attrs={'class':'form-control form-control-user','placeholder':''}),
        }
    

class CreateTopicForm(forms.ModelForm):
    instructor = forms.ModelChoiceField(get_user_model().objects.all(), widget=forms.Select(attrs={'class':'form-control form-control-user'}))
    class Meta:
        model = Topic
        fields= '__all__'
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control form-control-user','placeholder':'Title'}),
            'course':forms.Select(attrs={'class':'form-control form-control-user','placeholder':'Course name'}),
            'contents':forms.Textarea(attrs={'class':'form-control','rows':'3' ,'id':'summernote'}),
            'levels':forms.Select(attrs={'class':'form-control form-control-user','placeholder':''}),
            'file':forms.FileInput(attrs={'class':'form-control form-control-user'})
        }
      

class TopicUpdateForm(forms.ModelForm):
     class Meta:
        model = Topic
        exclude = ['instructor']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control form-control-user','placeholder':'Title'}),
            'course':forms.Select(attrs={'class':'form-control form-control-user','placeholder':'Course name'}),
            'contents':forms.Textarea(attrs={'class':'form-control','rows':'3','id':'summernote'}),
            'levels':forms.Select(attrs={'class':'form-control form-control-user','placeholder':''}),
            'file':forms.FileInput(attrs={'class':'form-control form-control-user'})
        }

        help_texts = {
            "file":"<p class='text-danger'>Note: Only uploads new files if you wish to change from existing one</p>"
        }