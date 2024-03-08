from dataclasses import asdict, dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Optional

import jwt

from application.settings import settings


@dataclass
class JWTPayload:
    """Payload for jwt token.

    iss (issuer): Issuer of the JWT
    sub (subject): Subject of the JWT (the user)
    aud (audience): Recipient for which the JWT is intended
    exp (expiration time): Time after which the JWT expires
    nbf (not before time): Time before which the JWT must not be accepted for processing
    iat (issued at time): Time at which the JWT was issued;
    can be used to determine age of the JWT
    jti (JWT ID): Unique identifier;
    can be used to prevent the JWT from being replayed
    (allows a token to be used only once)
    """

    iss: Optional[str]
    sub: Optional[str]
    exp: Optional[datetime]
    iat: Optional[datetime]
    aud: str = field(init=False)
    nbf: datetime = field(init=False)
    jti: str = field(init=False)


def create_access_token(identify: str) -> str:
    """Create access token.

    :param identify: Issuer of the JWT.
    :return: token.
    """
    token_payload = JWTPayload(
        iss=identify,
        sub="access_token",
        exp=datetime.now(timezone.utc) + timedelta(seconds=settings.jwt_expires),
        iat=datetime.now(timezone.utc),
    )
    payload = asdict(token_payload)
    payload = {key: value for key, value in payload.items() if value is not None}

    return jwt.encode(
        payload,
        settings.jwt_secret,
        algorithm=settings.jwt_algorithm,
    )


def decode_token(token: str) -> dict[str, str]:
    """
    Decode access token.

    :param token: token.
    :return: decoded data.
    """
    return jwt.decode(token, settings.jwt_secret, algorithms=[settings.jwt_algorithm])
