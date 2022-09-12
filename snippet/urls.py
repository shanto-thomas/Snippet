"""snippet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

from textdata import views
from rest_framework import routers

from textdata.views import RegisterusersViewSet, UpdateSnippetViewSet, addingSnippetViewSet, viewListOfSnippetViewSet, \
    DeleteSnippetViewSet, ListTagViewSet, tagDetailsViewSet, totalCountListViewSet

router = routers.DefaultRouter()

router.register(r'register', RegisterusersViewSet, basename='register')
router.register(r'addingSnippet', addingSnippetViewSet, basename='addingSnippet')
router.register(r'viewListOfSnippet', viewListOfSnippetViewSet, basename='viewListOfSnippet')
router.register(r'updateSnippet', UpdateSnippetViewSet, basename='updateSnippet')
router.register(r'deleteSnippet', DeleteSnippetViewSet, basename='deleteSnippet')
router.register(r'listTag', ListTagViewSet, basename='listTag')
router.register(r'tagDetails', tagDetailsViewSet, basename='tagDetails')
router.register(r'totalCountList', totalCountListViewSet, basename='totalCountList')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/login', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),

]
