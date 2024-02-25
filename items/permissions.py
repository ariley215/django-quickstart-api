from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: # hover over SAFE_METHODS to see which qualify
            return True

        # if we're allowing the purchaser to be null in Model
        # then this will check for that case and allow access
        if obj.owner is None:
            return True

        return obj.owner == request.user
