from typing import Optional

import strawberry

from application.web.gql.auth.resolvers import login_user, register_user
from application.web.gql.auth.schema import Token
from application.web.gql.user.schema import User


@strawberry.type
class Mutation:
    """Mutations for provider."""

    register: Optional[User] = strawberry.mutation(
        resolver=register_user,
        description="Create user in a database",
        permission_classes=[],
    )

    login: Token = strawberry.mutation(
        resolver=login_user,
        description="Login user.",
        permission_classes=[],
    )
