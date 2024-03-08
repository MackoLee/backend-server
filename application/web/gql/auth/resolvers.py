from typing import Any, Optional

from strawberry.types import Info

from application.db.dao.user_dao import UserDao
from application.db.models.user_model import UserModel
from application.provider.crypt_provider import hash_password, verify_password
from application.provider.jwt_provider import create_access_token
from application.web.gql.auth.schema import LoginInput, RegisterInput, Token
from application.web.gql.context import Context
from application.web.gql.user.resolvers import resolve_user_model
from application.web.gql.user.schema import User


async def register_user(
    root: Any,
    info: Info[Context, None],
    data: RegisterInput,
) -> Optional[User]:
    """Register a user.

    :param root: root.
    :param info: connection info.
    :param data: data.
    :return: user.
    """
    user_dao = UserDao(info.context.db_connection)
    user_model = UserModel(
        user_id=data.user_id,
        email=data.email,
        name=data.name,
        hashed_password=hash_password(data.password),
    )
    user_model = await user_dao.create(user_model=user_model)
    return resolve_user_model(user_model, info)


async def login_user(
    root: Any,
    info: Info[Context, None],
    data: LoginInput,
) -> Token:
    """Login user.

    :param root: root.
    :param info: connection info.
    :param data: data.
    :return: token: token.

    :raises ValueError: if user not found or invalid password.
    :raises ValueError: if invalid password.
    """
    user_dao = UserDao(info.context.db_connection)
    user_model = await user_dao.get_by_email(email=data.email)
    if user_model is None:
        raise ValueError("User not found")
    if not verify_password(data.password, user_model.hashed_password):
        raise ValueError("Invalid password")

    return Token(
        access_token=create_access_token(user_model.user_id),
        refresh_token=create_access_token(user_model.user_id),
        type="JWT",
        expires_in=3600,
    )
