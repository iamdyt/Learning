from django.urls import path
from .import views



app_name = 'users'

urlpatterns = [
    path("instructor/sign-up/", views.Register.as_view(), name="instructor_register"),
    path("instructor/sign-in/", views.Login.as_view(), name="instructor_login"),
    path("instructor/dashboard/",views.Dashboard .as_view(), name="instructor_dashboard"),

    #Students
    path("student/sign-up/", views.Register.as_view(), name="student_register"),
    path("student/sign-in/", views.Login.as_view(), name="student_login"),
    path("student/dashboard/",views.Dashboard .as_view(), name="student_dashboard"),
]
