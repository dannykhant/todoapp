"""OpenAPI config for app.  See OpenAPISettings for configuration."""

from litestar.openapi.config import OpenAPIConfig
from litestar.openapi.spec import Contact

config = OpenAPIConfig(
    title="todoapp",
    version="0.0.1",
    contact=Contact(email="dannypmkhant@gmail.com"),
    use_handler_docstrings=True,
    root_schema_site="swagger",
)
