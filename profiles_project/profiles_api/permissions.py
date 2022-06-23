from rest_framework import permissions

class UpdateOwnprofile(permissions.BasePermission):
    """allo user to edit their own profile"""
    def has_object_permission(self, request, view, obj): #every time api is being called it will pass the request, view and object for which we are trying to chejc the persmsison
        """check user is trying to edit thierown profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id
        