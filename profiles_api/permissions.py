from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profiles"""

    def has_object_permission(self, request, view, obj):
        """Check if the user is the owner"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to edit their own profiles"""

    def has_object_permission(self, request, view, obj):
        """Check if the user is the owner"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile.id == request.user.id
