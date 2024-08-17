from fastapi import FastAPI, Query, Path, Body
from typing import Annotated


app = FastAPI()

search_query = Query(min_length=5, max_length=10, examples=['salomat'])


@app.get('/category')
async def search_category(search: Annotated[str, search_query]):
    return {"searched text": search}


@app.post("/news/{news_id}")
async def get_news(
    news_id: Annotated[int, Path(gt=10, le=20, examples=[11, 12, 15])],
    name: Annotated[str, Body(min_length=5, max_length=15, examples=['Asadbek', 'Akbarjon'], embed=True)]
):
    data = {
        "success": True,
        "status": "200",
        "news_id": news_id,
        "name": name
    }
    return data
