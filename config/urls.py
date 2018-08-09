from django.conf.urls import url, include
from rest_framework import routers
from project.api import views
from project.api.webViews import index


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
urlpatterns = [
    url(r'', index, name='homePage'),
]

