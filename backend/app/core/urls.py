from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet, MenuViewSet

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet)
router.register(r'menus', MenuViewSet)

urlpatterns = [
    path('', include(router.urls)),
]