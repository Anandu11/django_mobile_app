"""Mobile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from phone.views import MobileView,MobileList,Mobiledetail,Mobileremove,Mobileupdate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/',MobileView.as_view()),
    path('mob/',MobileList.as_view(),name="lst"),
    path('mob/<int:k>',Mobiledetail.as_view(),name="detail"),#representing the ID of the mobile phone entry
    path('mob/<int:k>/remove',Mobileremove.as_view(),name="remove"),
    #, which handles the deletion of a specific mobile phone entry.
    path('mob/<int:pk>/update',Mobileupdate.as_view(),name="change"),


]














