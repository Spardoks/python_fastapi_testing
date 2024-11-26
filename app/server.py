from typing import List

import crud
import models
import schema
from dependency import SessionDependency
from fastapi import FastAPI
from lifespan import lifespan

app = FastAPI(
    title="Advertisement",
    description="Cервис объявлений купли/продажи",
    version="0.1",
    lifespan=lifespan,
)


@app.post("/advertisement", response_model=schema.CreateAdvertismentResponse)
async def create_advertisement(
    session: SessionDependency,
    create_advertisement_request: schema.CreateAdvertismentRequest,
):
    create_advertisement_dict = create_advertisement_request.dict()
    advertisement = models.Advertisement(**create_advertisement_dict)
    await crud.add_item(session, advertisement)
    return advertisement.id_dict


@app.patch(
    "/advertisement/{advertisement_id}",
    response_model=schema.UpdateAdvertismentResponse,
)
async def update_advertisement(
    session: SessionDependency,
    advertisement_id: int,
    update_advertisement_request: schema.UpdateAdvertismentRequest,
):
    advertisement = await crud.get_item_by_id(
        session, models.Advertisement, advertisement_id
    )
    advertisement_dict = update_advertisement_request.dict(exclude_none=True)
    for field, value in advertisement_dict.items():
        setattr(advertisement, field, value)
    await crud.add_item(session, advertisement)
    return advertisement.id_dict


@app.delete("/advertisement/{advertisement_id}")
async def delete_advertisement(session: SessionDependency, advertisement_id: int):
    await crud.delete_item(session, models.Advertisement, advertisement_id)
    return {"status": "success"}


@app.get(
    "/advertisement/{advertisement_id}", response_model=schema.GetAdvertismentResponse
)
async def get_advertisement_by_id(session: SessionDependency, advertisement_id: int):
    advertisement = await crud.get_item_by_id(
        session, models.Advertisement, advertisement_id
    )
    return advertisement.dict


@app.get("/advertisement", response_model=List[schema.GetAdvertismentResponse])
async def get_advertisement_by_query(
    session: SessionDependency,
    title: str = None,
    author: str = None,
    description: str = None,
    price: str = None,
):
    advertisements = await crud.get_item_by_query(
        session,
        models.Advertisement,
        title=title,
        author=author,
        description=description,
        price=price,
    )
    return [ad.dict for ad in advertisements]
