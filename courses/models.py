from django.db import models
from django.contrib.auth import get_user_model,get_user
from django.urls import reverse
# Create your models here.

class Course(models.Model):
    choice = (('ND-I','ND-I'),('ND-II','ND-II'),('HND-I','HND-I'),('HND-II','HND-II'))
    sess = (('1st-session','1st-session'),('2nd-session','2nd-session'))
    sem = (('1st-semester','1st-semester'),('2nd-semester','2nd-semester'))
    rate = (('difficult','Difficult'),('easy','Easy'))
    course_code = models.CharField(max_length=10)
    course_name = models.CharField(max_length=25)
    description = models.TextField(max_length=900, default='Lorem Ipsum')
    instructor = models.ForeignKey(get_user_model(),on_delete=models.SET_NULL, null=True, db_constraint=False)
    level = models.CharField(choices=choice, max_length=8)
    session = models.CharField(choices=sess,max_length=15)
    semester = models.CharField(choices=sem,max_length=15)
    levels = models.CharField(choices=rate, max_length=10)
    file = models.FileField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_name
    
    def get_absolute_url(self):
        return reverse("courses:course_view", kwargs={"pk": self.pk})
    


class Topic (models.Model):
    rate = (('difficult','Difficult'),('easy','Easy'))
    title = models.CharField(max_length=25)
    contents = models.TextField(max_length=1000)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    instructor = models.OneToOneField(get_user_model(),on_delete=models.SET_NULL, null=True)
    file = models.FileField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    levels = models.CharField(choices=rate, max_length=10)

    def get_absolute_url(self):
        return reverse("courses:topic_view", kwargs={"pk": self.pk})
    
    