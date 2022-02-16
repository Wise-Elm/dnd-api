from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('ability', views.AbilityScoreViewSet)
router.register('damage', views.DamageTypeViewSet)
router.register('equipment', views.EquipmentViewSet)
router.register('equipment-category', views.EquipmentViewSet)
router.register('skill', views.SkillViewSet)
router.register('weapon', views.WeaponViewSet)
router.register('weapon-property', views.WeaponPropertyViewSet)

urlpatterns = router.urls
