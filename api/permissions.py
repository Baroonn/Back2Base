from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    message = "You cannot delete what you did not create"
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.agent == request.user