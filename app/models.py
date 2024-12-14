from datetime import UTC, datetime
from sqlalchemy import TIMESTAMP, Column
from sqlmodel import Field, SQLModel


class PostBase(SQLModel):
    title: str
    content: str


class Post(PostBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
        sa_column=Column(
            TIMESTAMP(timezone=True), nullable=True, default=datetime.now(UTC)
        ),
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
        sa_column=Column(
            TIMESTAMP(timezone=True), nullable=True, onupdate=datetime.now(UTC)
        ),
    )


class PostsResponse(SQLModel):
    """Response model for Posts query."""
