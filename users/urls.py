from django.urls import path
from .import views



app_name = 'users'

urlpatterns = [
    path("instructor/sign-up/", views.Register.as_view(), name="instructor_register"),
    path("instructor/sign-in/", views.Login.as_view(), name="instructor_login"),
    path("instructor/dashboard/",views.Dashboard.as_view(), name="instructor_dashboard"),
    path("", views.Home.as_view(), name="index"),

    #Students
    path("student/sign-up/", views.StudentRegister.as_view(), name="student_register"),
    path("student/sign-in/", views.StudentLogin.as_view(), name="student_login"),
    path("student/dashboard/",views.StudentDashboard.as_view(), name="student_dashboard"),
    path("profile/<int:pk>/",views.Instructor_Profile.as_view(), name="instructor_profile"),
    path("student/profile/<int:pk>/",views.Student_Profile.as_view(), name="student_profile"),
    path("logout/",views.Logout.as_view(), name="logout"),
    path("logout/student/",views.Student_Logout.as_view(), name="student_logout")
]
