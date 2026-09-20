from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI(title="k-feasibility",version="0.3.0")
class Query(BaseModel): query:str
@app.get("/health")
def health(): return {"status":"ok","project":"k-feasibility","version":"0.3.0"}
@app.post("/analyze")
def analyze(req:Query): return {"domain":"feasibility","query":req.query,"checks":["demand","cost","funding","scenario"],"status":"prototype"}
