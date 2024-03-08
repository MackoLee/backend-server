import strawberry

from application.web.gql.permission import IsAdminOrAccountOwnerPermission
from application.web.gql.user import resolvers
from application.web.gql.user.schema import User


@strawberry.type
class Mutation:
    """Mutations for users."""

    update_user: User = strawberry.mutation(
        resolver=resolvers.update_user,
        description="Update a user.",
        permission_classes=[
            IsAdminOrAccountOwnerPermission,
        ],
    )

    delete_user: User = strawberry.mutation(
        resolver=resolvers.delete_user,
        description="Delete a user.",
        permission_classes=[
            IsAdminOrAccountOwnerPermission,
        ],
    )
