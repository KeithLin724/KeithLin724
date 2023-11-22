import httpx  
import asyncio
import json
from rich import print
from pydantic import BaseModel 
from typing import Optional , Union


class Repo(BaseModel):
    name : str
    html_url : str
    description : Optional[str] = ""
    stargazers_count : int
    forks_count : int
    license : Optional[dict[str,str]] = None
    topics : Optional[list[str]] = None
    clone_url : str
    language : Optional[Union[str , list[str]]] = None
    
    # @classmethod
    # def make_from_dict(cls , json_item_dict : dict):
    #     repo_name = json_item_dict.get("name" , "")
    #     html_url = json_item_dict.get("html_url" , "")
    #     description = json_item_dict.get("description" , "")
    #     stargazers_count = json_item_dict.get("stargazers_count" , "")
    #     forks_count = json_item_dict.get("forks_count" , "")
    #     license_type = json_item_dict.get("license" , "")
    #     topics = json_item_dict.get("topics" , "")
    #     clone_url = json_item_dict.get("clone_url" , "")
    #     language = json_item_dict.get("language" , "")
        
    #     return cls(repo_name , html_url,description , stargazers_count, forks_count,license_type)
    @staticmethod
    async def parse_obj_with_async(obj):
        return await asyncio.to_thread(Repo.parse_obj, obj)
    
        

async def get_github(user_name):
    COMMAND_FUNC = f"https://api.github.com/users/{user_name}/repos"
    
    async with httpx.AsyncClient() as client:
        res  = await client.get(COMMAND_FUNC)
    
    return  res.json()

async def main():
    user_name = "KeithLin724"
    result_json = await get_github(user_name=user_name)
    res = json.dumps(result_json)
    
    with open("test.json" , mode="w") as f:
        f.write(res)
        
        
    # print(result_json[0])
    # obj = Repo.parse_raw(json.dumps(result_json[0]))
    # obj = Repo.parse_obj(result_json[0])
    # print(obj)
    # get = await Repo.parse_obj_with_async(result_json[0])
    
    result_json = list(filter(lambda obj : obj['fork'] == False , result_json))

    
    # for i , obj in enumerate(result_json):
    #     get = await Repo.parse_obj_with_async(obj)
    #     print(i)
    #     print(get)
    
    # print(get)
    tasks = [
        Repo.parse_obj_with_async(obj)
        for obj in result_json
    ]
    
    res_async = await asyncio.gather(*tasks)
    print(res_async)
    with open("test_1.json" , mode="w") as f:
        f.write(res)
    
    return


asyncio.run(main())