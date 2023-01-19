"""cv_admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from cv_admin import settings
from cv_app import views
from django.urls import path
from django.conf.urls import static

urlpatterns = [
    path('', views.index, name="home"),
    path('index/', views.index),
    path('index/delete/', views.index_delete),
    path('signup/', views.signup),
    path('login/', views.login),
    path('error_pwd/', views.error_pwd),
    path('upload/', views.upload),
    path('manage/', views.manage),
    path('manage/follow/', views.manage_follow),
    path('manage/cancel/', views.manage_cancel),
    path('manage/delete/', views.manage_delete),
    path('logout/', views.logout),
    path('error/', views.error),
    path('success/', views.success),

]

urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
