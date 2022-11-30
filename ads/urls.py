from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter

from ads.views import AdViewSet, CommentViewSet

ads_router = SimpleRouter()
ads_router.register("ads", AdViewSet, basename="ads")

comment_router = NestedSimpleRouter(ads_router, 'ads', lookup='ad')
comment_router.register('comments', CommentViewSet, basename="comments")

urlpatterns = [
    path('', include(ads_router.urls)),
    path('', include(comment_router.urls)),
]
