from django.urls import path
from imgpro import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:id>/', views.categories, name='categories')
]
