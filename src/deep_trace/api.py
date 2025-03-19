from fastapi import FastAPI, Query
from typing import Optional
from .crew import DeepTraceCrew

deep_trace=DeepTraceCrew().crew()
app = FastAPI()

@app.get("/search")
async def  search(name: str = Query(..., description="User's name"),
           phone: str = Query(..., description="User's phone number"),
           context: Optional[str] = Query("", description="Optional extra information")):

    inputs = {"name":name,
             "phone": phone,
             "context": context}

    deep_trace_crew = DeepTraceCrew()
    crew = deep_trace_crew.crew()
#     results = crew.kickoff(inputs=inputs)
    results = await crew.kickoff_async(inputs=inputs)

    return results.pydantic


@app.get("/")
def read_root():
    return {"Hello": "World"}
