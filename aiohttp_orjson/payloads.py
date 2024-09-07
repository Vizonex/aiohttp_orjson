from typing import Any, Union, Optional
from aiohttp import BytesPayload
from orjson import dumps



class OrJsonPayload(BytesPayload):
    def __init__(self, 
        value: Union[bytes, bytearray, memoryview[int]], 
        option:Optional[int] = None,
        # Orjson already spits out utf-8
        # FROM ORJSON README: "has strict UTF-8 conformance, more correct than the standard library"
        encoding = "utf-8",
        content_type: str = "application/json",
        *args: Any, 
        **kwargs: Any
        ) -> None:

        super().__init__(
            dumps(value),
            encoding=encoding  
            content_type=content_type,
            *args, 
            **kwargs
        )



