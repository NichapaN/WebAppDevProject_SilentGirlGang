"""
URL configuration for silentgirlgang project.

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
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
<<<<<<< HEAD:silentgirlgang/silentgirlgang/urls.py
from django.urls import path, include
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tpopstore/', include('tpopstore.urls')),    
    path('buyers/', include('buyers.urls')),
    path('sellers/', include('sellers.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
=======
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tpopstore.urls', namespace='tpopstore')),
    path('basket/', include('basket.urls', namespace='basket')),
>>>>>>> 19f786edaec8950aab9fa19b2001adb1840a5a07:silentgirlgang/urls.py
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
