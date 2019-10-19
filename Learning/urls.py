from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
import courses,users
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('users.urls', namespace='users')),
    path("courses/", include('courses.urls',namespace='courses'))
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)