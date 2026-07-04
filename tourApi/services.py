from rest_framework.permissions import BasePermission


class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        try:
            return obj.author == request.user
        except:
            return 0

