
from django.contrib import admin
from django.urls import path, include
# from Note_API import views
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('Note', views.Note_APIViewSet, basename='Note')
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(router.urls)),
    path('', include('Note_API.urls')),

]
