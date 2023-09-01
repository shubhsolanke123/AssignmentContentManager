
from rest_framework import permissions

class IsAuthororAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.userdetails == request.user or request.user.is_staf


    def has_object_permission(self, request, view, obj):
        return obj.userdetails == request.user



