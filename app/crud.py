from fastapi import HTTPException
from models import ORM_CLS, ORM_OBJECT
from sqlalchemy import and_, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession


async def add_item(session: AsyncSession, item: ORM_OBJECT):
    session.add(item)
    try:
        await session.commit()
    except IntegrityError as err:
        if err.orig.pgcode == "23505":
            raise HTTPException(status_code=409, detail="Item already exists")
        raise err


async def get_item_by_id(
    session: AsyncSession, orm_cls: ORM_CLS, item_id: int
) -> ORM_OBJECT:
    orm_obj = await session.get(orm_cls, item_id)
    if orm_obj is None:
        raise HTTPException(status_code=404, detail="item not found")
    return orm_obj


async def get_item_by_query(
    session: AsyncSession,
    orm_cls: ORM_CLS,
    title: str,
    description: str,
    author: str,
    price: str,
) -> ORM_OBJECT:

    filters = []
    if title is not None:
        filters.append(orm_cls.title == title)
    if author is not None:
        filters.append(orm_cls.author == author)
    if description is not None:
        filters.append(orm_cls.description == description)
    if price is not None:
        filters.append(orm_cls.price == price)

    query = select(orm_cls).where(and_(*filters))
    result = await session.execute(query)
    advertisements = result.scalars().all()

    if advertisements is None:
        raise HTTPException(status_code=404, detail="item not found")
    return advertisements


async def delete_item(session: AsyncSession, orm_cls: ORM_CLS, item_id: int):
    orm_obj = await get_item_by_id(session, orm_cls, item_id)
    await session.delete(orm_obj)
    await session.commit()