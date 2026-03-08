

from rest_framework import permissions


class IsActiveStaffUser(permissions.BasePermission):
    """
    Разрешает доступ только активным сотрудникам (is_active и is_staff).
    """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.is_active and
            request.user.is_staff
        )