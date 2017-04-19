from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import SezioniViewSet, UsersViewSet, CentriDiRaccoltaViewSet


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', UsersViewSet)
router.register(r'sezioni', SezioniViewSet)
router.register(r'centridiraccolta', CentriDiRaccoltaViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', views.obtain_auth_token),
]
