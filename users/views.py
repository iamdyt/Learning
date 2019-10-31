from django.shortcuts import render,redirect    
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, View
from django.contrib.auth.views  import LoginView
from django.contrib.auth import get_user_model,logout
from courses.models import Course,Topic
from .forms import StaffRegForm, Student_Profile, StaffLoginForm, StudentRegForm, StudentRegForm, StudentLoginForm, Instructor_Profile
from django.db.models import Q

# Create your views here.
class Register (CreateView):
    model = get_user_model()
    template_name = 'users/instructor/signup.html'
    form_class = StaffRegForm


    def get_success_url (self):
        url = reverse_lazy('users:instructor_login')
        return url
    

class Login (LoginView):
    template_name = 'users/instructor/login.html'
    form_class = StaffLoginForm

    def get_success_url(self):
        success_url = reverse_lazy('users:instructor_dashboard')
        return success_url


class Dashboard (TemplateView):
    template_name = 'users/instructor/dashboard/index.html'
    def get_context_data(self, **kwargs):
        # self.request.session['lect'] = get_user_model().objects.get(username=self.request.user)
        context = super().get_context_data(**kwargs)
        context["incourse"] = Course.objects.filter(instructor=self.request.user).count()
        context["intopic"] = Topic.objects.filter(instructor=self.request.user).count()
        context["courses"] = Course.objects.filter(instructor=self.request.user)[:5]
        context['topics'] = Topic.objects.filter(instructor=self.request.user)[:5]

        return context

class StudentRegister (CreateView):
    model = get_user_model()
    template_name = 'users/student/signup.html'
    form_class = StudentRegForm
    success_url = reverse_lazy('users:student_login')

class StudentLogin (LoginView):
    template_name = 'users/student/login.html'
    form_class = StudentLoginForm

    def get_success_url(self):
        # level = self.request.POST['level']
        # result = self.request.POST['prev_result']
        # self.request.session['level'] = level
        # self.request.session['result'] =result
        
        url = reverse_lazy('users:student_dashboard')
        return url

class StudentDashboard (TemplateView):
    template_name = 'users/student/dashboard/index.html'
    def get_context_data(self, **kwargs):
        # self.request.session['lect'] = get_user_model().objects.get(username=self.request.user)
        context = super().get_context_data(**kwargs)
        context["incourse"] = Course.objects.filter(level=self.request.user.level).count()
        context["intopic"] = Topic.objects.filter(Q(levels=self.request.user.prev_result) & Q(course__level=self.request.user.level)).count()
        context["courses"] = Course.objects.filter(level=self.request.user.level)[:5]
        context['topics'] = Topic.objects.filter(Q(levels=self.request.user.prev_result) | Q(course__level=self.request.user.level))[:5]
        # context['']

        return context

class Instructor_Profile(UpdateView):
    model = get_user_model()
    template_name = 'users/instructor/dashboard/profile.html'
    form_class = Instructor_Profile


class Student_Profile(UpdateView):
    model = get_user_model()
    template_name = 'users/student/dashboard/profile.html'
    form_class = Student_Profile

class Logout(View):
    def get (self,request):
        logout(self.request)
        return redirect('users:instructor_login', permanent=True)

class Student_Logout(View):
    def get (self,request):
        logout(self.request)
        return redirect('users:student_login', permanent=True)