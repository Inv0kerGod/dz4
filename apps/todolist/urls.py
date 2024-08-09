from rest_framework.routers import DefaultRouter

from .views import TaskViewSet


router = DefaultRouter()
router.register('task', TaskViewSet, basename="task_api")

urlpatterns = router.urls    
