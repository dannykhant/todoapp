from litestar import Litestar, get

from advanced_alchemy.exceptions import RepositoryError

from app import domain
from app.lib import database, repository, exceptions, dependencies

dependencies = dependencies.create_collection_dependencies()

app = Litestar(route_handlers=[*domain.routes],
               dependencies=dependencies,
               exception_handlers={RepositoryError: exceptions.exception_to_http_response},
               openapi_config=domain.openapi.config,
               plugins=[database.plugin, domain.plugins.pydantic],
               on_app_init=[repository.on_app_init])
