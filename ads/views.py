from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, pagination
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser

from ads.filter import AdFilter
from ads.models import Ad, Comment
from ads.permissions import AdUpdatePermission
from ads.serializers import AdSerializer, AdDetailSerializer, CommentSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    pagination_class = AdPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdFilter

    def get_serializer_class(self):
        if self.action in ['retrieve', 'me']:
            return AdDetailSerializer
        else:
            return AdSerializer

    def get_permissions(self):
        if self.action in ['update', 'destroy', 'me']:
            self.permission_classes = [AdUpdatePermission]
        return super().get_permissions()

    def perform_create(self, serializer):
        """
        Создание объявления
        """
        serializer.save(author=self.request.user)

    def get_queryset(self):
        if self.action == 'me':
            return Ad.objects.filter(author=self.request.user).all()
        return Ad.objects.all()

    @action(detail=False)
    def me(self, request, *args, **kwargs):
        self.queryset = Ad.objects.filter(author=request.user.pk)
        return super().list(self, request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        ad_id = self.kwargs.get('ad_pk')
        ad_instance = get_object_or_404(Ad, id=ad_id)
        return ad_instance.comments.all()

    def perform_create(self, serializer):
        ad_id = self.kwargs.get('ad_pk')
        ad_instance = get_object_or_404(Ad, pk=ad_id)
        user = self.request.user
        serializer.save(author=user, ad=ad_instance)
