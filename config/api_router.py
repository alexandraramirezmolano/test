from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from djsniper.users.api.views import UserViewSet
#from djsniper.sniper.views import ProjectViewset, CategoryViewset, OrdersViewset
from djsniper.users.api.views import (
    RoleViewSet,
    CustomGroupViewSet,
    CustomPermissionViewSet,
    UserViewSet,
    PaymentMethodViewSet,
    CoalBonusViewSet,
    ProjectViewSet,
    PurchaseOrderViewSet,
)

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
#router.register("projects", ProjectViewset)
#router.register("categories", CategoryViewset)
#router.register("orders", OrdersViewset)

router.register(r'roles', RoleViewSet)
router.register(r'groups', CustomGroupViewSet)
router.register(r'permissions', CustomPermissionViewSet)
router.register(r'users', UserViewSet)
router.register(r'payment-methods', PaymentMethodViewSet)
router.register(r'coal-bonuses', CoalBonusViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'purchase-orders', PurchaseOrderViewSet)

app_name = "api"
urlpatterns = router.urls
