
from django.contrib import admin
from django.urls import path,include
from contentapp import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router=DefaultRouter()
router.register('content',views.StudentModelViewset,basename='content')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(router.urls)),
    path('v1/', include('authapp.urls')),
    path('token/',obtain_auth_token)
    
]
