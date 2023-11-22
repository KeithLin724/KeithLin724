import asyncio
from pydantic import BaseModel
from typing import Optional, Union


class Repo(BaseModel):
    name: str
    html_url: str
    description: Optional[str] = ""
    stargazers_count: int
    forks_count: int
    license: Optional[dict[str, str]] = None
    topics: Optional[list[str]] = None
    clone_url: str
    language: Optional[Union[str, list[str]]] = None


    @staticmethod
    async def parse_obj_with_async(obj):
        return await asyncio.to_thread(Repo.parse_obj, obj)

    @staticmethod
    async def parse_list_of_obj_with_async(list_of_obj):
        tasks = [Repo.parse_obj_with_async(obj) for obj in list_of_obj]

        return await asyncio.gather(*tasks)