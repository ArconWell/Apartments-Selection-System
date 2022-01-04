"""apartmentsSelectionSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from selectionApartments import views

urlpatterns = [
    path('', views.index, name='home'),
    re_path(r'^about/$', views.about),
    re_path(r'^about/(?P<counter_value>\d+)/', views.about),
    path('contact/<str:user_name>', views.contact),
    path('contact/', views.contact),
    path('admin/', admin.site.urls),
]