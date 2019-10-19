
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView
from .models import Topic,Course
from django.core.exceptions import ObjectDoesNotExist
from .forms import CreateCourseForm, CourseUpdateForm, CreateTopicForm, TopicUpdateForm


# Create your views here.
class CourseAdd (CreateView):
    template_name = 'users/instructor/courses/create.html'
    form_class = CreateCourseForm
    success_url = reverse_lazy('users:instructor_dashboard')

    # def get_initial(self):
    #     initial = super().get_initial()
    #     user =  get_user_model().objects.get()
    #     initial['instructor'] =user.pk
    #     return initial

class CourseAll (ListView):
    template_name = 'users/instructor/courses/all.html'
    context_object_name ='courses'
    def get_queryset(self):
        queryset = Course.objects.filter(instructor=self.request.user)
        return queryset

class CourseSingle (DetailView):
    template_name = 'users/instructor/courses/single.html'
    model = Course
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        try:
            topik = Topic.objects.filter(course=self.object.pk).count()
            context['topic'] = topik
            return context
        except ObjectDoesNotExist:
            return context

class CourseUpdate(UpdateView):
    model = Course
    form_class = CourseUpdateForm
    template_name = 'users/instructor/courses/edit.html'
    
      
class TopicAdd (CreateView):
    model = Topic
    form_class = CreateTopicForm
    template_name = 'users/instructor/topics/create.html'


class TopicAll(ListView):
    template_name = 'users/instructor/topics/all.html'
    context_object_name = 'topics'
    def get_queryset(self):
        queryset = Topic.objects.filter(instructor=self.request.user)
        return queryset

class TopicSingle (DetailView):
    model = Topic
    template_name = 'users/instructor/topics/single.html'
    context_object_name = 'topic'

class TopicUpdate(UpdateView):
    model = Topic
    template_name = 'users/instructor/topics/edit.html'
    form_class = TopicUpdateForm