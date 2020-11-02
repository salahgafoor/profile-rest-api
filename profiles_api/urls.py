from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,base_name='hello-viewset')#name of url
router.register('profile',views.UserProfileViewSet) #no need of base_name since there is a queryset
router.register('feed',views.UserProfileFeedViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('',include(router.urls)),
    path('login/', views.UserLoginApiView.as_view()),

]
