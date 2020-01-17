"""untitled7 URL Configuration

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
from untitled7.shitu import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('look/', view.book),
    path('', view.index),
    path('bookurl/', view.bookurl)

]
# 'default': {
#     'ENGINE': 'django.db.backends.mysql',
#     'NAME': 'ceshi',
#     'USER': 'root',
#     'PASSWORD': 'root',
#     'HOST': '127.0.0.1',
#     'PORT': 3306,
# }