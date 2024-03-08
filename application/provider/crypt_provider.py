from passlib.context import CryptContext

context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(
    plain_password: str,
    hashed_password: str,
) -> bool:
    """Verify password.

    :param plain_password: Plain password.
    :param hashed_password: Hashed password.
    :return: True if password is verified, False otherwise.
    """
    return context.verify(plain_password, hashed_password)


def hash_password(password: str) -> str:
    """Hash password.

    :param password: Password.
    :return: Hashed password.
    """
    return context.hash(password)
