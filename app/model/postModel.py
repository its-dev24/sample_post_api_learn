from pydantic import BaseModel,Field
from typing import Optional

class Post(BaseModel):
    id : int
    title : str
    content : str
    published : bool
    # rating : Optional[int]

class UpdatePost(BaseModel):
    title : Optional[str] = Field(default = None)
    content : Optional[str] = Field(default = None)
    published :Optional[str] = Field(default = None)
    # rating : Optional[str] = Field(default = None)
    
