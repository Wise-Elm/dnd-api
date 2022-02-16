import debug_toolbar
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

admin.site.site_header = 'D&D 5E Admin'
admin.site.index_title = 'Admin'

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('playground/', include('playground.urls')),
    path('items/', include('items.urls'))
]
