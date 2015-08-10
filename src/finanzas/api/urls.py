from django.conf.urls import patterns, url, include
from rest_framework_nested import routers

from finanzas.authentication.viewsets import AccountViewSet


router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

urlpatterns = patterns(
    '',
    url(r'^v1/', include(router.urls)),
)
