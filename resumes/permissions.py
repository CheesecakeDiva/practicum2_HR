from rest_framework.permissions import BasePermission, SAFE_METHODS


class ResumePermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser or (request.user.role and request.user.role.name == "Администратор"):
            return True

        if request.user.role and request.user.role.name == "HR-менеджер":
            return request.method in SAFE_METHODS

        return obj.user == request.user
