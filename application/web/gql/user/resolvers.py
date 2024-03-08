from typing import Any, AsyncIterator, Optional, Sequence

from strawberry.types import Info

from application.db.dao.user_dao import UserDao
from application.db.models.user_model import UserModel
from application.web.gql.context import Context
from application.web.gql.user.schema import DeleteUserInput, UpdateUserInput, User


def resolve_user_model(
    root: UserModel,
    info: Info[Context, None],
) -> User:
    """Get user by id.

    :param root: root.
    :param info: connection info.
    :return: user.
    """
    return User(
        code=str(root.id),
        email=root.email,
        name=root.name,
        is_active=root.is_active,
        is_superuser=root.is_superuser,
        is_verified=root.is_verified,
        created_at=root.created_at,
        updated_at=root.updated_at,
    )


async def get_users(
    root: Any,
    info: Info[Context, None],
    order_by: Optional[str] = None,
    where: Optional[str] = None,
) -> AsyncIterator[User]:
    """Get all users.

    :param root: root.
    :param info: connection info.
    :param order_by: order by.
    :param where: where.

    :yields: user.
    """
    user_dao = UserDao(info.context.db_connection)
    users: Sequence[UserModel] = await user_dao.get_all()
    for user in users:
        yield resolve_user_model(user, info)


async def update_user(
    root: Any,
    info: Info[Context, None],
    data: UpdateUserInput,
) -> Optional[User]:
    """Update a user.

    :param root: root.
    :param info: connection info.
    :param data: data.
    :return: user.
    """
    user_dao = UserDao(info.context.db_connection)
    user_model = await user_dao.get_by_id(id=int(data.id.node_id))
    if user_model is None:
        return None

    for attr, value in data.__dict__.items():
        if value is not None:
            setattr(user_model, attr, value)

    return resolve_user_model(user_model, info)


async def delete_user(
    root: Any,
    info: Info[Context, None],
    data: DeleteUserInput,
) -> bool:
    """Delete a user.

    :param root: root.
    :param info: connection info.
    :param data: data.
    :return: True if user is deleted.
    """
    user_dao = UserDao(info.context.db_connection)
    user_model = await user_dao.delete_by_id(id=data.id)

    return user_model is not None
