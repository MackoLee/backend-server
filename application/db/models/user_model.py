from sqlalchemy import BigInteger, Sequence
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import Boolean, String

from application.db.base import Base


class UserModel(Base):
    """User model."""

    __tablename__ = "users"

    id_seq = Sequence(f"{__tablename__}_id_seq")
    id: Mapped[int] = mapped_column(
        BigInteger,
        id_seq,
        primary_key=True,
        server_default=id_seq.next_value(),
    )
    user_id: Mapped[str] = mapped_column(
        String(length=100),
        unique=True,
        nullable=False,
    )
    email: Mapped[str] = mapped_column(String(length=100), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(length=100))
    hashed_password: Mapped[str] = mapped_column(String(length=255))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False)
