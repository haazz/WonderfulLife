"""
URL configuration for WonderfulLife project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('meditation/', include('meditation.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from WonderfulLife import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('meditation/', include('meditation.urls')),
    path('community/', include('community.urls')),
    path('markdownx/', include('markdownx.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('single_pages.urls')),
    path('timer/', include('timer.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
