from fastapi import FastAPI
from fastapi import applications
from fastapi.openapi.docs import get_swagger_ui_html
from contextlib import asynccontextmanager

from core.models import db_helper, Base
from api import router as api_router


def swagger_monkey_patch(*args, **kwargs):
    # SwaggerUI long loading fix
    return get_swagger_ui_html(
        *args, **kwargs,
        swagger_js_url="https://cdn.staticfile.net/swagger-ui/5.1.0/swagger-ui-bundle.min.js",
        swagger_css_url="https://cdn.staticfile.net/swagger-ui/5.1.0/swagger-ui.min.css")

applications.get_swagger_ui_html = swagger_monkey_patch


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(api_router, prefix="/api")