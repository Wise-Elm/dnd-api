import debug_toolbar
from django.urls import include, path
from . import views

urlpatterns = [
    path('weapon/', views.weapon_list),
    path('weapon-detail/<int:id>/', views.weapon_detail),
    path('ability/', views.ability_score_list),
    path('ability-detail/<int:id>/', views.ability_score_detail),
    path('skill/', views.skill_list),
    path('skill-detail/<int:id>/', views.skill_detail),
    path('damage/', views.damage_type_list),
    path('damage-detail/<int:id>', views.damage_type_detail),
    path('weapon-property/', views.weapon_property_list),
    path('weapon-property-detail/<int:id>', views.weapon_property_detail)
]