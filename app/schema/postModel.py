from pydantic import BaseModel,Field
from typing import Optional

class Post(BaseModel):
    title : str
    content : str
    published : bool = True
    # rating : Optional[int]

class createPost(Post):
    pass

class UpdatePost(BaseModel):
    title : Optional[str] = Field(default = None)
    content : Optional[str] = Field(default = None)
    published :Optional[bool] = Field(default = None)
    # rating : Optional[str] = Field(default = None)
    
class PostResp(Post):
    id : int