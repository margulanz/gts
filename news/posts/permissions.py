from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """
    def has_permission(self, request, view):
        # Allow GET, HEAD, OPTIONS requests for any user (read-only access)
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Allow POST requests only if the user is authenticated
        if request.method == 'POST':
            return request.user and request.user.is_authenticated
        
        # For other methods (PUT, DELETE, etc.), require authentication
        return request.user and request.user.is_authenticated
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.author == request.user