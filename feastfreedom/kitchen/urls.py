"""feastfreedom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include, re_path

from . import views
from kitchen.views import KitchenListView, KitchenCreateView, KitchenDetailView, KitchenUpdateView, KitchenDeleteView

app_name = 'kitchen'

urlpatterns = [
    #path('', HomePageView.as_view(), name='home'),
    path('', views.home, name='home'),
    path('check', views.check, name='check'),
    re_path(r'kitchen/$', KitchenListView.as_view(), name='index'),
    #path('', KitchenListView.as_view(), name='index'),
    path('kitchen/create', KitchenCreateView.as_view(), name='kitchen_create'),
    path('kitchen/<pk>', KitchenDetailView.as_view(), name='kitchen_detail'),
    path('kitchen/<pk>/update', KitchenUpdateView.as_view(), name='kitchen_update'),
    path('kitchen/<pk>/delete', KitchenDeleteView.as_view(), name='kitchen_delete'),
]

