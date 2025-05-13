from fastapi import APIRouter

router = APIRouter()

@router.get("items/{item_id}")
async def get_items(item_id:int):
    return { item_id: item_id}