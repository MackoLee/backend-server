from typing import Any

from strawberry.permission import BasePermission
from strawberry.types import Info

from application.web.gql.context import Context


class IsAdminPermission(BasePermission):
    """Check if user is admin."""

    def has_permission(
        self,
        source: Any,
        info: Info[Context, None],
        **kwargs: Any,
    ) -> bool:
        """Check if user is admin.

        :param source: source.
        :param info: info.
        :param kwargs: kwargs.
        :return: True if user is admin.
        """
        return True


class IsAdminOrAccountOwnerPermission(BasePermission):
    """Check if user is admin or account owner."""

    def has_permission(
        self,
        source: Any,
        info: Info[Context, None],
        **kwargs: Any,
    ) -> bool:
        """Check if user is admin or account owner.

        :param source: source.
        :param info: info.
        :param kwargs: kwargs.
        :return: True if user is admin or account owner.
        """
        return True
