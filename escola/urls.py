from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('alunos.urls')),
    path('admin/', admin.site.urls),
    # http://127.0.0.1:8000/auth/login/
    # http://127.0.0.1:8000/auth/logout
    path('auth/', include('rest_framework.urls')),
]
