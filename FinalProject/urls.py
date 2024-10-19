"""
URL configuration for FinalProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from Quest.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Menu_page),
    path('Enter/', Enter_page),
    path('Redactor/', Redactor_page),
    path('create/', Create_player_page),
    path('Player/', Player_page),
    path('Battel/', Battel_page),
    path('Location/', Location_page),
    path('Gameover/', Gameover_page),
    path('Move/', Move_request),
    path('Enter_dungeon/', Enter_dungeon_page),
    path('Winning_page/', Winning_page),
    path('Trap/', Trap_page),
    path('Riddle/', Riddel_page),
    path('Redactor/Location/', Redactor_location_page),
    path('Redactor/Class/', Redactor_class_page),
    path('Redactor/Inventory/', Redactor_inventory_page),
    path('Redactor/Enemy/', Redactor_enemy_page),
    path('Redactor/Enemy/Skill/', Redactor_enemy_skill_page),
    path('Redactor/Item/', Redactor_item_page),
]
