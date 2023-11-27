from rest_framework import permissions


class IsNotAuthenticated(permissions.BasePermission):
    """
    인증되지 않은 사용자만 허용하는 사용자 지정 권한 클래스입니다.

    Args:
    - message (str): 권한이 거부될 때 표시할 메시지입니다.
    """

    message = "이미 인증된 사용자입니다."

    def has_permission(self, request, view):
        """
        요청을 하는 사용자가 인증되지 않은지 확인합니다.

        Return:
        - bool: 사용자가 인증되지 않았으면 True, 그렇지 않으면 False입니다.
        """
        return not request.user.is_authenticated


class PostOnlyAccess(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST":
            return True
