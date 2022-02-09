import debug_toolbar
from django.urls import include, path
from . import views

urlpatterns = [
    path('weapon/', views.weapon_list),
    path('weapon/<int:id>/', views.weapon_detail),
    path('ability/', views.ability_score_list),
    path('ability/<int:id>/', views.ability_score_detail),
    path('skill/', views.skill_list),
    path('skill/<int:id>/', views.skill_detail),
    path('damage/', views.damage_type_list),
    path('damage/<int:id>/', views.damage_type_detail),
    path('weapon-property/', views.weapon_property_list),
    path('weapon-property/<int:id>/', views.weapon_property_detail),
    path('equipment/', views.equipment_list),
    path('equipment/<int:id>/', views.equipment_detail),
    path('equipment-category/', views.equipment_category_list),
    path('equipment-category/<int:id>/', views.equipment_category_detail)
]