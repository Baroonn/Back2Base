from rest_framework import permissions
from django.contrib.auth.models import AnonymousUser

class IsOwnerOrReadOnly(permissions.BasePermission):
    message = "You cannot delete what you did not create"

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.agent == request.user

class IsAdminOrCreateOnly(permissions.BasePermission):
    message = "Only admins can view all agents"

    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        if type(request.user) is not AnonymousUser:
            return request.user.is_staff
        else: 
            return False

class IsAgentOrReadOnly(permissions.BasePermission):
    message = "You cannot delete or make changes to another agent"
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj == request.user