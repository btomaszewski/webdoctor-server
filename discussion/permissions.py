from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only the owner of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read is always allowed so allow GET, HEAD and OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True

        # Only give write perms to owner
        return obj.owner == request.user
