from sqlmodel import Session

from app.models import Post


def init(session: Session):
    """"""
    for i in range(300):
        post = Post(title=f"Post: {i}", content=f"GreatPost: {i}")
        session.add(post)
