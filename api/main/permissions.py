from rest_framework.permissions import SAFE_METHODS, BasePermission

class IsAdminOrReadonly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif request.method == "DELETE":
            return request.user.role == 'admin'
        return request.user and request.user.role in ['user', 'admin']
