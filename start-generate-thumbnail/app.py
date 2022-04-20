import datetime
import time
from typing import Optional, Dict

import uvicorn
from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.responses import JSONResponse, Response

from application_property_loader import load_application_property
from logger import logger
from thumbnail_generater import generate_thumbnail
from thumbnail_request import ThumbnailRequest

api: FastAPI = FastAPI(
    title='Start Generate Thumbnail API',
    version='1.0.0'
)


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        start_time: float = time.time()
        logger.info(f'process start! {datetime.time()}')

        if request.query_params:
            logger.info(f'query parameters= {request.query_params}')

        try:
            response = await call_next(request)
        except Exception as exception:
            logger.info(f'process failed!= {exception}')
            return JSONResponse(content=dict(message='process failed'), status_code=500)

        logger.info(f'process end!= {int(time.time() - start_time) % 60}')
        return response


api.add_middleware(RequestLoggingMiddleware)


@api.get("/api/greeting")
async def greeting() -> Dict[str, str]:
    return dict(message='greeting')


@api.get('/api/video/thumbnail')
async def get_thumbnail(request: ThumbnailRequest, second: Optional[int] = 0) -> Dict[str, str]:
    generate_thumbnail(
        filename=request.filename,
        file_store_path=request.file_store_path,
        thumbnail_name=request.thumbnail_name,
        thumbnail_store_path=request.thumbnail_store_path,
        target_second=second
    )
    return dict(message='process success')


if __name__ == "__main__":
    application_property = load_application_property()
    uvicorn.run(api, host=application_property.host, port=application_property.port)
