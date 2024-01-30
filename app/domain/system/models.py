from dataclasses import dataclass

from typing import Literal


@dataclass
class HealthStatus:
    app_status: Literal["online", "offline"]
    db_status: Literal["online", "offline"]
