from django.urls import path
from . import views

urlpatterns = [
    path('ability/', views.AbilityScoreList.as_view()),
    path('ability/<int:pk>/', views.AbilityScoreDetail.as_view()),
    path('damage/', views.DamageTypeList.as_view()),
    path('damage/<int:pk>/', views.DamageTypeDetail.as_view()),
    path('equipment/', views.EquipmentList.as_view()),
    path('equipment/<int:pk>/', views.EquipmentDetail.as_view()),
    path('equipment-category/', views.EquipmentCategoryList.as_view()),
    path('equipment-category/<int:pk>/', views.EquipmentCategoryDetail.as_view()),
    path('skill/', views.SkillList.as_view()),
    path('skill/<int:pk>/', views.SkillDetail.as_view()),
    path('weapon/', views.WeaponList.as_view()),
    path('weapon/<int:pk>/', views.WeaponDetail.as_view()),
    path('weapon-property/', views.WeaponPropertyList.as_view()),
    path('weapon-property/<int:pk>/', views.WeaponPropertyDetail.as_view())
]