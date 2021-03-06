"""maasite URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls'))
]

admin.site.site_header = '塭仔圳市地重劃區（第一區）PCM 管線協調'
admin.site.site_title = 'PCM管線協調'
# Use include() to add paths from the catalog application

urlpatterns += [
    path('pipelines/', include('pipelines.urls')),
]

# Add URL maps to redirect the base URL to our application
urlpatterns += [
    path('', RedirectView.as_view(url='pipelines/', permanent=True)),
]

# Use static() to add URL mapping to serve static files during development (only)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
