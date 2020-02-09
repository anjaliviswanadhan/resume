"""anjaliresumeproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from mainapp import views as v1
from personalapp import views as v2
from professionalapp import views as v3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('disp1/',v1.disp1_data),
    path('disp2/',v2.disp2_data),
    path('disp3/',v3.disp3_data),
    path('disp4/',v3.disp4_data),
]
