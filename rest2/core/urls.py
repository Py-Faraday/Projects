from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include ('mainapp.urls')),
    path('rest-auth/', include('rest_framework.urls')),

]
