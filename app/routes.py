from fastapi import APIRouter
from pydantic import AwareDatetime
from app.deps import SessionDep

router = APIRouter(prefix="/post")


@router.get("/")
def posts(
    session: SessionDep,
    max_result: int,
    start_at: AwareDatetime,
    end_at: AwareDatetime,
    pagenation_token: str,
):
    pass
