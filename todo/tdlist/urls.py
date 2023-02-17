from rest_framework.routers import DefaultRouter
from tdlist.views import TasklistViewSet

router = DefaultRouter()

router.register(
    prefix="tdlist",
    viewset=TasklistViewSet,
    basename="tdlist",
)

urlpatterns = router.urls
