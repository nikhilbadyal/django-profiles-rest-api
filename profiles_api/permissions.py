from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit only their own profiles"""

    def has_object_permission(self, request, view, obj):
        """Check if user has access to update details"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id
