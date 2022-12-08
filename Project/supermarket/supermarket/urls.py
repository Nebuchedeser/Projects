"""supermarket URL Configuration

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
from django.urls import path
from .views import home, item_list, item_detail, category_list, subcategory_list, register, profile, profile_update

urlpatterns = [
    path('', home, name='home'),
    path('items', item_list, name='item_list'),
    path('items/<int:id>', item_detail, name='item_detail'),
    path('categories', category_list, name='category_list'),
    path('categories/<int:category_id>/subcategories', subcategory_list, name='subcategory_list'),
    path('register', register, name='register'),
    path('profile', profile, name='profile'),
    path('profile/update', profile_update, name='profile_update'),
]


