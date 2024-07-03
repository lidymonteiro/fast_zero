from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    new_user = User(
        username='ada', email='ada@lovelace.com', password='M1nh@S3nh@'
    )

    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'ada'))

    assert user.username == 'ada'
