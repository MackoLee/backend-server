import strawberry
from strawberry.fastapi import GraphQLRouter

from application.web.gql import auth, user
from application.web.gql.context import Context, get_context


@strawberry.type
class Query(  # noqa: WPS215
    user.Query,
    auth.Query,
):
    """Main query."""


@strawberry.type
class Mutation(  # noqa: WPS215
    user.Mutation,
    auth.Mutation,
):
    """Main mutation."""


schema = strawberry.Schema(
    Query,
    Mutation,
)

gql_router: GraphQLRouter[Context, None] = GraphQLRouter(
    schema,
    graphiql=True,
    context_getter=get_context,
)
