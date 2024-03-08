import datetime
from typing import Annotated

import strawberry
from strawberry.relay.types import NodeIDPrivate

relay = strawberry.relay


@strawberry.type
class User(relay.Node):
    """User model."""

    code: Annotated[str, NodeIDPrivate()] = relay.NodeID

    email: str
    name: str
    is_active: bool
    is_superuser: bool
    is_verified: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime


@strawberry.type
class UserConnection(relay.ListConnection[User]):
    """User connection."""


@strawberry.input
class UpdateUserInput:
    """User input."""

    id: strawberry.relay.GlobalID
    email: str
    name: str
    is_active: bool
    is_superuser: bool
    is_verified: bool


@strawberry.input
class DeleteUserInput:
    """User input."""

    id: strawberry.relay.GlobalID
