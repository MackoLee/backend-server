import strawberry

from application.web.gql.permission import IsAdminPermission
from application.web.gql.user.resolvers import get_users
from application.web.gql.user.schema import UserConnection


@strawberry.type
class Query:
    """Query to interact with provider."""

    users: UserConnection = strawberry.relay.connection(
        resolver=get_users,
        description="Get all users.",
        permission_classes=[
            IsAdminPermission,
        ],
    )
