import httpx
import asyncio
import json
from rich import print
from pydantic import BaseModel
from typing import Optional, Union


class User(BaseModel):
    GITHUB_API = lambda user_name: f"https://api.github.com/users/{user_name}"
    name: str
    login: str
    # icon
    avatar_url: Optional[str] = ""
    html_url: str
    followers: int
    # info
    bio: str
    company: Optional[str] = ""
    location: str
    public_repos: int
    public_gists: int

    @staticmethod
    async def parse_obj_with_async(obj):
        return await asyncio.to_thread(User.parse_obj, obj)


async def main() -> None:
    user_name = "KeithLin724"

    async with httpx.AsyncClient() as client:
        response = await client.get(User.GITHUB_API(user_name))

    result = response.json()

    obj = await User.parse_obj_with_async(result)
    print(obj)
    return


asyncio.run(main())
