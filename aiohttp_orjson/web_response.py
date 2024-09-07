from typing import Optional, Any, Callable

from aiohttp.web_response import Response
from orjson import dumps
from aiohttp.helpers import sentinel
from aiohttp.typedefs import LooseHeaders


def orjson_response(
    data: Any = sentinel,
    option:Optional[int] = None,
    default:Optional[Callable[[Any], Any]] = None,
    *,
    text: Optional[str] = None,
    body: Optional[bytes] = None,
    status: int = 200,
    reason: Optional[str] = None,
    headers: Optional[LooseHeaders] = None,
    content_type: str = "application/json"
) -> Response:
    """Sends a json response using orjson to dump the data off"""
    if data is not sentinel:
        if text or body:
            raise ValueError("only one of data, text, or body should be specified")
        else:
            body = dumps(data, default=default, option=option)
    
    return Response(
        text=text,
        body=body,
        status=status,
        reason=reason,
        headers=headers,
        content_type=content_type,
    )



