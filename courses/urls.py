from django.urls import path
from .import views
app_name ='courses'

urlpatterns = [
    ## Course Routes
    path('add/',views.CourseAdd.as_view(),name='course_add'),
    path("all/",views.CourseAll .as_view(), name="course_all"),
    path("view/<int:pk>/",views.CourseSingle.as_view(), name="course_view"),
    path("edit/<int:pk>/",views.CourseUpdate.as_view(), name="course_update"),

    ## Topic Routes
    path("topic/add/",views.TopicAdd.as_view(), name="topic_add"),
    path("topic/all/",views.TopicAll.as_view(), name="topic_all"),
    path("topic/view/<int:pk>/",views.TopicSingle.as_view(), name="topic_view"),
    path("topic/edit/<int:pk>/",views.TopicUpdate.as_view(), name="topic_update"),

    #StudentCourses/Topics
    path("student/all/",views.StudentCourses.as_view(), name="student_courses"),
    path("student/view/<int:pk>/",views.StudentCoursesingle.as_view(), name="student_course_single"),
    path("student/topics/",views.StudentTopics.as_view(), name="student_topics"),
    path("student/topic/view/<int:pk>/",views.StudentTopicsingle.as_view(), name="student_topic_single")
]