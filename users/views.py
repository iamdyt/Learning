from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView
from django.contrib.auth.views  import LoginView
from django.contrib.auth import get_user_model
from courses.models import Course,Topic
from .forms import StaffRegForm, StaffLoginForm

# Create your views here.
class Register (CreateView):
    model = get_user_model()
    template_name = 'users/instructor/signup.html'
    form_class = StaffRegForm
    success_url = reverse_lazy('users:instructor_login')

class Login (LoginView):
    template_name = 'users/instructor/login.html'
    form_class = StaffLoginForm

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
        