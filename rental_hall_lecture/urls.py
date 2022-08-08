"""rental_hall_lecture URL Configuration

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
from django.urls import path
from hall_lecture.views import (
    main_site,
    add_hall,
    list_all_halls,
    hall_details,
    hall_modify,
    hall_booked,
    hall_delete,

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', main_site),
    path('room/new', add_hall),
    path('room/list-all', list_all_halls),
    path('room/<int:hall_id>', hall_details),
    path('room/modify/<int:hall_id>', hall_modify),
    path('room/reserve/<int:hall_id>', hall_booked),
    path('room/delete/<int:hall_id>', hall_delete),
]
