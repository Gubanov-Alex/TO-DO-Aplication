from django.contrib import admin
from django.urls import include,path
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings

from users.views import UserViewSet

from tasks.views import TaskViewSet

# from tasks.views import TasksViewSet

router = DefaultRouter()
router.register('users', UserViewSet,basename='user')
router.register('tasks', TaskViewSet,basename='task')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='access_token_refresh'),
    path('', include(router.urls)),
]

if settings.DEBUG is True:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root = settings.MEDIA_ROOT
    )
