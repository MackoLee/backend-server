import strawberry


@strawberry.input
class RegisterInput:
    """Register input."""

    email: str
    name: str
    user_id: str
    password: str


@strawberry.input
class LoginInput:
    """Login input."""

    email: str
    password: str


@strawberry.type
class Token:
    """Token model."""

    access_token: str
    refresh_token: str
    type: str
    expires_in: int
