import asyncio
from pydantic import BaseModel
from typing import Optional, Union


class Repo(BaseModel):
    GITHUB_API = lambda user_name: f"https://api.github.com/users/{user_name}/repos"
    # project name
    name: str
    # github page
    html_url: str
    description: Optional[str] = ""
    # star counter
    stargazers_count: int
    forks_count: int
    # license
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
