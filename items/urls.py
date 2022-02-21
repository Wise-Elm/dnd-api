from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('ability', views.AbilityScoreViewSet,
                basename='ability')
router.register('damage', views.DamageTypeViewSet,
                basename='damage')
router.register('equipment', views.EquipmentViewSet,
                basename='equipment')
router.register('equipment-category', views.EquipmentCategoryViewSet,
                basename='equipment-category')
router.register('skill', views.SkillViewSet,
                basename='skill')
router.register('weapon', views.WeaponViewSet,
                basename='weapon')
router.register('weapon-property', views.WeaponPropertyViewSet,
                basename='weapon-property')
router.register('weapon-type', views.WeaponTypeViewSet,
                basename='weapon-property')

urlpatterns = router.urls
