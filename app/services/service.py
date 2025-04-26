import os
from fastapi.responses import JSONResponse

class Service:
    def response(self, code: int, message: str, data: any = None, error: any = None):
        return JSONResponse(
            status_code=code,
            content={
                "status": True,
                "data": data,
                "message": message if code != 500 or os.getenv('DEBUG') else "Request failed due to an internal error.",
                "error": error,
            },
        )
