from fastapi import FastAPI, Query, status
from typing import Optional
from deep_trace.models import HealthCheck, Profile
from deep_trace.app import deep_trace



app = FastAPI()


@app.get("/search")
async def  search(full_name: str = Query(..., description="User's full name"),
           phone: str = Query(..., description="User's phone number"),
           context: Optional[str] = Query("", description="Optional extra information")) -> Profile:

    inputs = {"full_name": full_name,
              "phone": phone,
              "context": context}

    return await deep_trace(inputs=inputs)


@app.get(
    "/health",
    tags=["healthcheck"],
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)
def get_health() -> HealthCheck:
    """
    ## Perform a Health Check
    Endpoint to perform a healthcheck on. This endpoint can primarily be used Docker
    to ensure a robust container orchestration and management is in place. Other
    services which rely on proper functioning of the API service will not deploy if this
    endpoint returns any other HTTP status code except 200 (OK).
    Returns:
        HealthCheck: Returns a JSON response with the health status
    """
    return HealthCheck(status="OK")
