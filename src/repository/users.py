from sqlalchemy.orm import Session

from src.database.models import User
from src.schemas import UserModel

from libgravatar import Gravatar


async def get_user_by_email(email: str, db: Session) -> User:
    """
    The get_user_by_email function takes in an email and a database session, then returns the user with that email.

    :param email: str: Get the email from the user
    :param db: Session: Pass a database session to the function
    :return: A user object if the email is found in the database
    """
    return db.query(User).filter(User.email == email).first()


async def create_user(body: UserModel, db: Session) -> User:
    """
    The create_user function creates a new user in the database.

    :param body: UserModel: Define the data that will be passed to the function
    :param db: Session: Pass in the database session
    :return: A user object
    :doc-author: Trelent
    """
    avatar = None
    try:
        g = Gravatar(body.email)
        avatar = g.get_image()
    except Exception as e:
        print(e)
    new_user = User(**body.dict(), avatar=avatar)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


async def update_token(user: User, token: str | None, db: Session) -> None:
    """
    The update_token function updates the refresh token for a user.

    :param user: User: Identify the user that is being updated
    :param token: str | None: Store the token in the database
    :param db: Session: Create a database session
    :return: None, but the return type is specified as str | none
    """
    user.refresh_token = token
    db.commit()

