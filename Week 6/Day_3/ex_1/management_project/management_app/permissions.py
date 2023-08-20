from rest_framework.permissions import BasePermission

class IsDepartmentAdmin(BasePermission):
    message = "You must be a department administrator to access this."

    def has_object_permission(self, request, view, obj):
        # Here, you'll need to define the logic to check if the user is a department administrator.
        # For the sake of this example, I'll assume that the user model has an attribute `is_department_admin`.
        return request.user.is_department_admin
