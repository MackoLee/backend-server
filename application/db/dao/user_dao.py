from typing import Any, Optional, Sequence

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from application.db.dependencies import get_db_session
from application.db.models.user_model import UserModel


class UserDao:
    """Data access object for user model."""

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    async def create(self, user_model: UserModel) -> UserModel:
        """Create a user.

        :param user_model: To be created user model
        :return: Created user model
        """
        self.session.add(user_model)
        await self.session.commit()
        return user_model

    async def get_by_id(
        self,
        **kwargs: Any,
    ) -> Optional[UserModel]:
        """Get user by id.

        :param kwargs: user id
        :return: Optional user model
        """
        return await self.session.get(UserModel, kwargs.get("id"))

    async def get_by_email(self, email: str) -> Optional[UserModel]:
        """Get user by email.

        :param email: email
        :return: user model
        """
        user = await self.session.execute(
            select(UserModel).filter(UserModel.email == email),
        )
        return user.scalar()

    async def delete_by_id(
        self,
        **kwargs: Any,
    ) -> Optional[UserModel]:
        """Delete user by u_id.

        :param kwargs: user id
        :return: deleted user model
        """
        user: Optional[UserModel] = await self.session.get(UserModel, kwargs.get("id"))
        if not user:
            return None

        await self.session.delete(user)
        await self.session.commit()
        return user

    async def get_all(self) -> Sequence[UserModel]:
        """Get all users.

        :return: all users
        """
        users = await self.session.scalars(select(UserModel))
        return users.all()
