from rest_framework import permissions

from users.managers import UserRoles


class AdUpdatePermission(permissions.BasePermission):
    message = 'Редактировать можно только свое объявление'

    def has_object_permission(self, request, view, obj):
        if request.user.role in [UserRoles.ADMIN]:
            return True

        return obj.author == request.user
