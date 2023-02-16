from rest_framework import permissions
import ipdb


class MyCustomUserPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.user == obj
            or request.user.is_authenticated
            and request.user.is_employee
        )
