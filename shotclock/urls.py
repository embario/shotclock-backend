from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from shotclock import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('music-profiles', views.MusicProfileViewSet)
router.register('power-hours', views.PowerHourViewSet)

schema_view = get_swagger_view(title='shotclock API')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/social-login/', views.SocialAuth.as_view(), name='social_login'),
    path('admin/', admin.site.urls),
    path('docs/', schema_view),
    path('api-auth/', include('rest_framework.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
