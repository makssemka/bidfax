from rest_framework.permissions import IsAuthenticated


class IsAdminOrIsSelf(IsAuthenticated):

    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id or request.user.is_superuser


class IsProfileOwner(IsAuthenticated):

    def has_object_permission(self, request, view, obj):
        return obj.user.id == request.user.id or request.user.is_superuser
