from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView
from django.contrib.auth.views  import LoginView
from django.contrib.auth import get_user_model
from courses.models import Course,Topic
from .forms import StaffRegForm, StaffLoginForm, StudentRegForm, StudentRegForm, StudentLoginForm
from django.db.models import Q

# Create your views here.
class Register (CreateView):
    model = get_user_model()
    template_name = 'users/instructor/signup.html'
    form_class = StaffRegForm


    def get_success_url (self):
        url = reverse_lazy('users:instructor_dashboard')
        return url
    

class Login (LoginView):
    template_name = 'users/instructor/login.html'
    form_class = StaffLoginForm
    success_url = reverse_lazy('users:instructor_dashboard')

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
