from typing import TypeVar, Literal

from litestar import Controller, get
from litestar.response import Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from app.domain.system.models import HealthStatus

OnlineOffline = TypeVar("OnlineOffline", bound=Literal["online", "offline"])


async def ping_db(db_session: AsyncSession):
    """Ping database to check the status"""

    try:
        await db_session.execute(text("select now()"))
        status = True
    except ConnectionError:
        status = False
    return status


class SystemController(Controller):
    tags = ["System"]

    @get(path="/health",
         operation_id="SystemHealth",
         name="health:system", )
    async def check_health_status(self, db_session: AsyncSession) -> Response[HealthStatus]:
        # noinspection PyTypeChecker
        db_status: OnlineOffline = "online" if await ping_db(db_session) else "offline"
        return Response(HealthStatus(app_status="online",
                                     db_status=db_status))
