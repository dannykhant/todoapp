from __future__ import annotations

from sqlalchemy.orm import Mapped, mapped_column

from app.lib.orm import TimestampedDatabaseModel

__all__ = ["TodoItem"]


class TodoItem(TimestampedDatabaseModel):
    """TodoItem."""

    # noinspection SpellCheckingInspection
    __tablename__: str = "item"
    __table_args__ = {"comment": "To store items to do."}
    title: Mapped[str] = mapped_column(index=False, nullable=False)
    done: Mapped[bool] = mapped_column(index=False, nullable=False)
